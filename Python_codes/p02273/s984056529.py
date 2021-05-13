import math

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

def koch(n, a, b):
    if n == 0:
        return 0

    s = Point(0, 0)
    t = Point(0, 0)
    u = Point(0, 0)
    th = math.pi * 60.0 / 180

    s.x = (2.0 * a.x + b.x) / 3
    s.y = (2.0 * a.y + b.y) / 3
    t.x = (a.x + 2.0 * b.x) / 3
    t.y = (a.y + 2.0 * b.y) / 3
    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y

    koch(n - 1, a, s)
    print("{:.6f} {:.6f}".format(s.x, s.y))
    koch(n - 1, s, u)
    print("{:.6f} {:.6f}".format(u.x, u.y))
    koch(n - 1, u, t)
    print("{:.6f} {:.6f}".format(t.x, t.y))
    koch(n - 1, t, b)

    return 0

a = Point(0.0, 0.0)
b = Point(100.0, 0.0)

n = int(input())

print("{:.6f} {:.6f}".format(a.x, a.y))
koch(n, a, b)
print("{:.6f} {:.6f}".format(b.x, b.y))