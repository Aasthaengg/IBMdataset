import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def koch(d, p1, p2):
    

    if d == 0:
        return
    
    t = Point((p1.x + 2 * p2.x )/3,(p1.y + 2 * p2.y )/3 )
    s = Point((p2.x + 2 * p1.x )/3,(p2.y + 2 * p1.y )/3 )
    
    u = Point((t.x-s.x) * (math.cos(math.pi / 3)) - (t.y-s.y) * (math.sin(math.pi / 3)) + s.x, (t.x-s.x) * (math.sin(math.pi / 3)) + (t.y-s.y) * (math.cos(math.pi / 3)) + s.y)
    #print(s.x, s.y , t.x, t.y, u.x, u.y)
    

    
    koch(d - 1, p1, s)
    print(s.x, s.y)
    koch(d - 1, s, u)
    print(u.x, u.y)
    koch(d - 1, u, t)
    print(t.x, t.y)
    koch(d - 1, t, p2)


n = int(input())
    
p1 = Point(0, 0)
p2 = Point(100, 0)

print(p1.x, p1.y)
koch(n, p1, p2)
print(p2.x, p2.y)


