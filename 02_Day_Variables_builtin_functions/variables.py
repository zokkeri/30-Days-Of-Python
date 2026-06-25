# Day 2: 30 Days of python programming

# Exercises: Level 1

first_name = "J"
last_name = "M"
full_name = first_name + last_name
country = "Sweden"
city = "Stockholm"
age = 33
year = 1993
is_married = True
is_true = True
is_light_on = False
this_var, that_var = 12, 31

# Exercises: Level 2

type(first_name)
type(last_name)
type(full_name)
type(country)
type(is_married)
type(this_var)

print(len(first_name))

print(len(first_name) > len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius**2
circum_of_circle = 3.14 * 2* radius
user_radius = float(input("Give radius"))
print("Area is: ", 3.14*user_radius**2)

user_first_names = input("Give first name: ")
user_last_name = input("Give last name: ")
user_age = input("Give user age: ")
user_country = input("Give country: ")

# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
