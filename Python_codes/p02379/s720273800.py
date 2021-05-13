import math

(x1, y1, x2, y2) = [float(i) for i in input().split()]

distance = math.hypot((x2 - x1), (y2 - y1))
print('{0:.5f}'.format(distance))