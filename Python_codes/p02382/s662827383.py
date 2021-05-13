import math
n = int(input())
v1 = map(float, input().split())
v2 = map(float, input().split())

v = [abs(x - y) for (x,y) in zip(v1, v2)]

d1 = sum(v)
d2 = math.sqrt(sum([x**2 for x in v]))
d3 = math.pow(sum([x**3 for x in v]), 1.0/3.0)
d4 = max(v)

print(d1)
print(d2)
print(d3)
print(d4)
