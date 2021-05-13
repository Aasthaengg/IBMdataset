import math
n = int(input())

start = (0,0)
end = (100,0)

def koch(n,p1,p2):
    if n == 0:
        return

    s = ( (p1[0]*2 + p2[0])/3, (p1[1] *2 + p2[1])/3 )
    t = ( (p1[0] + p2[0]*2)/3, (p1[1] + p2[1] *2)/3 )

    ux = (t[0] - s[0])/2 - (t[1] - s[1])*math.sqrt(3)/2 + s[0]
    uy = (t[0] - s[0])*math.sqrt(3)/2 + (t[1] - s[1])/2 + s[1]
    u = (ux, uy)
    koch(n-1,p1, s)
    ppp(s)
    koch(n-1, s, u)
    ppp(u)
    koch(n-1, u, t)
    ppp(t)
    koch(n-1, t,p2)

def ppp(t):
    print("{:.08f} {:.08f}".format(t[0],t[1]))

ppp(start)
koch(n,start,end)
ppp(end)

