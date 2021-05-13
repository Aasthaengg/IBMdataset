import math

L, R, d = map(int, input().split())

l = math.ceil(L / d)
r = math.floor(R / d)

print(r - l + 1)