import math

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

x1, y1, x2, y2 = [float(i) for i in input().split()]

point1 = Point(x1, y1)
point2 = Point(x2, y2)

x_dist = point1.x - point2.x
y_dist = point1.y - point2.y

dist = math.sqrt(x_dist ** 2 + y_dist ** 2)

print(dist)
