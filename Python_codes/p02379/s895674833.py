from math import hypot

a, b, c, d = map(float, input().split())
e = hypot((a-c), (b-d))
print(e)