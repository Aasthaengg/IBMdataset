from math import ceil
x = int(input())
print(2 * (x // 11) + ceil(x % 11 / 6))