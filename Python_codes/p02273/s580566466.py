# -*- coding: utf-8 -*-

import math

class Point_Class:
    def __init__(self, x, y):
        self.x  =   x
        self.y  =   y

    def printPoint(self):
        print "%f %f" %(self.x, self.y)

def koch(n, p1, p2):
    if n == 0:
        return
    sin60 = math.sin(math.radians(60))
    cos60 = math.cos(math.radians(60))
    s = Point_Class((2*p1.x+p2.x)/3, (2*p1.y+p2.y)/3)
    t = Point_Class((p1.x+2*p2.x)/3, (p1.y+2*p2.y)/3)
    u = Point_Class((t.x-s.x)*cos60-(t.y-s.y)*sin60+s.x, (t.x-s.x)*sin60+(t.y-s.y)*cos60+s.y)
    koch(n-1, p1, s)
    s.printPoint()
    koch(n-1, s, u)
    u.printPoint()
    koch(n-1, u, t)
    t.printPoint()
    koch(n-1, t, p2)

n = int(raw_input())
p1 = Point_Class(0.0, 0.0)
p2 = Point_Class(100.0, 0.0)
p1.printPoint()
koch(n, p1, p2)
p2.printPoint()