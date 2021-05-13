import math
def koch(d, p1, p2):
    if d == 0:
        return
    x=p2[0]-p1[0]
    y=p2[1]-p1[1]
    s = [(p1[0]*2+p2[0]*1)/3.0,(p1[1]*2+p2[1]*1)/3.0]
    t = [(p1[0]*1+p2[0]*2)/3.0,(p1[1]*1+p2[1]*2)/3.0]
    u = [p1[0]+x/2-y*math.sqrt(3)/6,p1[1]+y/2+x*math.sqrt(3)/6]
    koch(d - 1, p1, s)
    print(*s)
    koch(d - 1, s, u)
    print(*u)
    koch(d - 1, u, t)
    print(*t)
    koch(d - 1, t, p2)
 
n = int(input())
p1=[0,0]
p2=[100,0]
print(*p1)
koch(n,p1,p2)
print(*p2)

