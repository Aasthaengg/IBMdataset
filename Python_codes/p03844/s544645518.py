input_string = input().split()
num1 = int(input_string[0])
num2 = int(input_string[2])
operater = input_string[1]

result = 0
if operater == "+":
    result = num1 + num2
elif operater == "-":
    result = num1 - num2

print(result)