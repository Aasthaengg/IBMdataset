str_input = input()
list_input = str_input.split(" ")
x = int(list_input[0])
y = int(list_input[1])
while y != 0:
    mod = x % y
    x = y
    y = mod
print(x)

