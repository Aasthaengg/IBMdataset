import math
x1, y1, x2, y2 = map(float, input().split())
print("{0:f}".format(math.sqrt((x1-x2)**2.0 + (y1-y2)**2.0)))
