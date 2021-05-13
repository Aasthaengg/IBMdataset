import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def koch(d, p1, p2):
    if d == 0:
        return

    else:
        s = Point()
        t = Point()
        u = Point()

        s.x = (2*p1.x + 1*p2.x)/3.0
        s.y = (2*p1.y + 1*p2.y)/3.0

        t.x = (1*p1.x + 2*p2.x)/3.0
        t.y = (1*p1.y + 2*p2.y)/3.0

        u.x = s.x + math.cos(math.radians(60)) * (t.x - s.x) - math.sin(math.radians(60)) * (t.y - s.y)
        u.y = s.y + math.sin(math.radians(60)) * (t.x - s.x) + math.cos(math.radians(60)) * (t.y - s.y)

        koch(d - 1, p1, s)
        print(s.x, s.y)
        koch(d - 1, s, u)
        print(u.x, u.y)
        koch(d - 1, u, t)
        print(t.x, t.y)
        koch(d - 1, t, p2)

def main():
    n = int(input())

    p1 = Point(0, 0)
    p2 = Point(100, 0)

    print(p1.x, p1.y)
    koch(n, p1, p2)
    print(p2.x, p2.y)

main()
