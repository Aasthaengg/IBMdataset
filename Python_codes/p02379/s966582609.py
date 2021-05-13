from enum import Enum

class Point():
    def __init__(self, arg_x, arg_y):
        self.x = arg_x
        self.y = arg_y

def calc_len(a, b):
    from math import sqrt
    return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y))

x1, y1, x2, y2 = map(float, input().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

print("%.10f"%calc_len(p1, p2))

