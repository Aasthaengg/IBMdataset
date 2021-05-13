import math

x = int(input())
a = x // 100
b = x % 100
print(1) if b <= 5*a else print(0)
