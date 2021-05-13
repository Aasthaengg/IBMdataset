import math

x1, y1, x2, y2 = [float(s) for s in input().split()]
print(math.sqrt((math.fabs(x1 - x2) ** 2) + (math.fabs(y1 - y2) ** 2)))