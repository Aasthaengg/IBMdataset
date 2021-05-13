import math
n = int(input())

x_min = n * 100 / 108
x_max = (n + 1) * 100 / 108

print(math.ceil(x_min) if math.ceil(x_min) < x_max else ':(')