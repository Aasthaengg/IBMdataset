import math

v = int(input())

cal = 100000
for w in range(v):
    cal = math.ceil(cal * 1.05 * 0.001) * 1000

print("%d" % cal)