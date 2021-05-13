from math import sqrt
x1, y1, x2, y2 = map(float, input().split())
r = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(r)