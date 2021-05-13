import math
n = int(input())
a = 100000
for _ in range(n):
    a *= 1.05
    a = 1000 * math.ceil(a / 1000)
print(a)

