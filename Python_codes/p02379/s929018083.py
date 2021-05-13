from math import sqrt

class  Point (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def d (p1, p2):
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

data = [float(e) for e in input().split()]
p1 = Point(data[0], data[1])
p2 = Point(data[2], data[3])

print(d(p1, p2))
