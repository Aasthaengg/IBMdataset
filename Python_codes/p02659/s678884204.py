import math

a, b = input().split()
a = int(a)
b = int(b.replace('.', ''))
a = a * b // 100
print(a)
