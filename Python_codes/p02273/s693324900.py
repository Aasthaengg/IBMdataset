import math

class dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def koch(n, p1, p2):
    if n != 0:
        r = 60.0*math.pi/180.0

        x = (2.0*p1.x+1.0*p2.x)/3.0
        y = (2.0*p1.y+1.0*p2.y)/3.0
        s = dot(x, y)

        x = (1.0*p1.x+2.0*p2.x)/3.0
        y = (1.0*p1.y+2.0*p2.y)/3.0
        t = dot(x, y)

        x = (t.x-s.x)*math.cos(r) - (t.y-s.y)*math.sin(r) + s.x
        y = (t.x-s.x)*math.sin(r) + (t.y-s.y)*math.cos(r) + s.y
        u = dot(x, y)

        koch(n-1, p1, s)
        print(s.x, ' ', s.y)
        koch(n-1, s, u)
        print(u.x, ' ', u.y)
        koch(n-1, u, t)
        print(t.x, ' ', t.y)
        koch(n-1, t, p2)


p1 = dot(0.0, 0.0)
p2 = dot(100.0, 0.0)
n = int(input())

print(p1.x, ' ', p1.y)
koch(n, p1, p2)
print(p2.x, ' ', p2.y)

