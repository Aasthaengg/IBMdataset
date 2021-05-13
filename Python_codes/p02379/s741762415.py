import math

x1, y1, x2, y2 = [float(line) for line in input().split()]
double_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(double_distance)

