import math
n = int(input())
s = 100000
r = 0.05
while n > 0:
    s += math.ceil((s * r) / 1000) * 1000
    n -= 1
print(s)