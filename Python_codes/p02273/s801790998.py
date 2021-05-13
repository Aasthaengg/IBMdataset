import math
def koch(n, p1, p2):
    if n == 0:
        return
    sx = (2*p1[0]+p2[0])/3
    sy = (2*p1[1]+p2[1])/3
    s = (sx, sy)
    tx = (p1[0]+2*p2[0])/3
    ty = (p1[1]+2*p2[1])/3
    t = (tx, ty)
    ux = (tx-sx)*math.cos(math.pi/3) - (ty-sy)*math.sin(math.pi/3) + sx
    uy = (tx-sx)*math.sin(math.pi/3) + (ty-sy)*math.cos(math.pi/3) + sy
    u = (ux, uy)
    koch(n-1, p1, s)
    print(s[0], s[1])
    koch(n-1, s, u)
    print(u[0], u[1])
    koch(n-1, u, t)
    print(t[0], t[1])
    koch(n-1, t, p2)
n = int(input())
p1 = (0, 0)
p2 = (100, 0)
print(0, 0)
koch(n, p1, p2)
print(100, 0)
