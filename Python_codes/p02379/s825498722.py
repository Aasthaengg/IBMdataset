import math
x1, y1, x2, y2 = [float(_) for _ in input().split()]
print(math.sqrt(pow((x2-x1), 2)+pow((y2-y1), 2)))