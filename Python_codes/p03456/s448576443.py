import math

input_string = input()
num = int(input_string.replace(' ', ''))

if math.sqrt(num) == int(math.sqrt(num)):
    print("Yes")
else:
    print("No")
