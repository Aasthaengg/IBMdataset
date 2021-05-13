import math

[x1, y1, x2, y2] = [float(x) for x in raw_input().split()]
print(math.sqrt((x2 - x1) ** 2.0 + (y2 - y1) ** 2.0))