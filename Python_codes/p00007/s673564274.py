import math

n = int(raw_input())
r = 100000
for i in range(n):
    r *= 1.05
    r = math.ceil(r/1000) * 1000
print int(r)