import math
x1, y1, x2, y2 = [int(a) for a in input().split()]

x = x2-x1
y = y2-y1

x3 = x2 - y
y3 = y2 + x

x4 = x1 - y
y4 = y1 + x

print(x3, y3, x4, y4)