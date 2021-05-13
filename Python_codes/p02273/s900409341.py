import math
n = int(input())
p1 = (0, 0)
p2 = (100, 0)

def kock(n, p1, p2):
    if n == 0:
        return
    
    sx = 2 / 3 * p1[0] + 1 / 3 * p2[0]
    sy = 2 / 3 * p1[1] + 1 / 3 * p2[1]
    s = (sx, sy)
    
    tx = 1 / 3 * p1[0] + 2 / 3 * p2[0]
    ty = 1 / 3 * p1[1] + 2 / 3 * p2[1]
    t = (tx, ty)
    
    ux = math.cos(math.radians(60)) * (tx-sx) - math.sin(math.radians(60)) * (ty-sy) + sx
    uy = math.sin(math.radians(60)) * (tx-sx) + math.cos(math.radians(60)) * (ty-sy) + sy
    u = (ux, uy)
    
    kock(n-1, p1, s)
    print (*s)
    kock(n-1, s, u)
    print (*u)
    kock(n-1, u, t)
    print (*t)
    kock(n-1, t, p2)
    
print(*p1)
kock(n, p1, p2)
print(*p2)
