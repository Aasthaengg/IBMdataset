from math import ceil
s = int(input())
print(0, 0, 10 ** 9, 1, abs(s - ((10 ** 9) * ceil(s / 10 ** 9))), ceil(s / 10 ** 9))