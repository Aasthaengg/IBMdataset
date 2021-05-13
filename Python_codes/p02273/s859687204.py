from decimal import Decimal
from math import cos, radians, sin



class Point():
    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)

    def output(self):
        print("{:.6f} {:.6f}".format(self.x, self.y))

    def calc_koch_apex(self, point):
        s_x = Decimal(2) / Decimal(3) * self.x + Decimal(1) / Decimal(3) * point.x
        s_y = Decimal(2) / Decimal(3) * self.y + Decimal(1) / Decimal(3) * point.y
        s = Point(s_x, s_y)

        t_x = Decimal(1) / Decimal(3) * self.x + Decimal(2) / Decimal(3) * point.x
        t_y = Decimal(1) / Decimal(3) * self.y + Decimal(2) / Decimal(3) * point.y
        t = Point(t_x, t_y)

        u_x = (t.x - s.x) * Decimal(cos(radians(60))) - \
              (t.y - s.y) * Decimal(sin(radians(60))) + s.x
        u_y = (t.x - s.x) * Decimal(sin(radians(60))) + \
              (t.y - s.y) * Decimal(cos(radians(60))) + s.y
        u = Point(u_x, u_y)

        return s, u, t


def kock(n, point1, point2):
    if n == 0:
        return


    s, u, t = point1.calc_koch_apex(point2)
    
    kock(n-1, point1, s)

    s.output()

    kock(n-1, s, u)

    u.output()

    kock(n-1, u, t)

    t.output()

    kock(n-1, t, point2)




n = int(input())

p1 = Point(0, 0)
p2 = Point(100, 0)


p1.output()

kock(n, p1, p2)

p2.output()

