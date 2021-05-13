import math

input_line = input().split()

A = int(input_line[0])
B = float(input_line[1])

result = (A * (B * 100)) /100

print(math.floor(result))