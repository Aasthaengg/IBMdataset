from math import sin
from math import cos
from math import pi

class point():
   def __init__(self,_x,_y):
       self.x = _x
       self.y = _y

def kock (n, p1, p2):
    if n == 0:
        return
    s = point((2. * p1.x + 1. * p2.x) / 3., (2. * p1.y + 1. *p2.y) / 3.)
    t = point((1. * p1.x + 2. * p2.x) / 3., (1. * p1.y + 2. *p2.y) / 3.)
    u = point((t.x - s.x) * cos(pi / 3.) - (t.y - s.y) * sin(pi / 3.) + s.x, (t.x - s.x) * sin(pi / 3.) + (t.y - s.y) * cos(pi / 3) + s.y)

    kock(n - 1, p1, s)
    print '%s %s' % (str(s.x), str(s.y))
    kock(n - 1, s, u)
    print '%s %s' % (str(u.x), str(u.y))
    kock(n - 1, u, t)
    print '%s %s' % (str(t.x), str(t.y))
    kock(n - 1, t, p2)

n = input();

p1 = point(0., 0.)
p2 = point(100., 0.)

print '%s %s' % (str(p1.x), str(p1.y))
kock(n, p1, p2)
print '%s %s' % (str(p2.x), str(p2.y))