import math

cos60=math.cos(math.radians(60))
sin60=math.sin(math.radians(60))

def knoc(n, l, r):
    if n == 0:
        return
    s = ((2*l[0]+r[0])/3, (2*l[1]+r[1])/3)
    t = ((l[0]+2*r[0])/3, (l[1]+2*r[1])/3)
    ux = (t[0]-s[0])*cos60-(t[1]-s[1])*sin60+s[0]
    uy = (t[0]-s[0])*sin60+(t[1]-s[1])*cos60+s[1]
    u = (ux, uy)
    
    knoc(n-1, l, s)
    print(s[0],s[1])
    knoc(n-1, s, u)
    print(u[0],u[1])
    knoc(n-1, u, t)
    print(t[0],t[1])
    knoc(n-1, t, r)
    
n = int(input())

start = (0,0)
end = (100,0)

print(start[0],start[1])
knoc(n, start, end)
print(end[0],end[1])
    
