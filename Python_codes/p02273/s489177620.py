import math


class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


def koch(n, p1, p2):
    if n == 0:
        return
    s, t, u = [Point() for _ in range(3)]
    s.x = (2 * p1.x + p2.x) / 3
    s.y = (2 * p1.y + p2.y) / 3
    t.x = (p1.x + 2 * p2.x) / 3
    t.y = (p1.y + 2 * p2.y) / 3
    a = math.radians(60)
    u.x = (t.x - s.x) * math.cos(a) - (t.y - s.y) * math.sin(a) + s.x
    u.y = (t.x - s.x) * math.sin(a) + (t.y - s.y) * math.cos(a) + s.y

    koch(n - 1, p1, s)
    print(s.x, s.y)
    koch(n - 1, s, u)
    print(u.x, u.y)
    koch(n - 1, u, t)
    print(t.x, t.y)
    koch(n - 1, t, p2)


p1 = Point(0, 0)
p2 = Point(100, 0)
n = int(input())
print(p1.x, p1.y)
koch(n, p1, p2)
print(p2.x, p2.y)

