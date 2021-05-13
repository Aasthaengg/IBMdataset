from math import ceil

inputs = input()
a = int(inputs.split(" ")[0])
b = int(inputs.split(" ")[1])
print(ceil((b - 1) / (a - 1)))
