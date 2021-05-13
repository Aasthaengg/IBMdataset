import math
cos60 = math.cos(60/180*math.pi)
sin60 = math.sin(60/180*math.pi)
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self.x) + " " + str(self.y)
        

def koch(n, p1, p2):
    if(n==0):
        return
    s = Point((2* p1.x + p2.x)/3, (2* p1.y + 1*p2.y)/3)
    
    t = Point((p1.x + 2* p2.x)/3, (p1.y + 2* p2.y)/3)
    
    u = Point((t.x - s.x)* cos60 - (t.y -s.y)* sin60 + s.x,
             (t.x - s.x)* sin60 + (t.y -s.y)* cos60 + s.y)
    
    koch(n-1, p1, s)
    print(s)
    koch(n-1, s, u)
    print(u)
    koch(n-1, u, t)
    print(t)
    koch(n-1, t, p2)

p1 = Point(0,0)
p2 = Point(100,0)
n = int(input())
print(p1)
koch(n, p1, p2)
print(p2)
