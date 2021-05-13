import math


def kock(n, p1, p2):
    if n == 0:
        return

    s = ((p1[0]*2 + p2[0]) / 3, (p1[1]*2 + p2[1]) / 3)
    t = ((p1[0] + p2[0]*2) / 3, (p1[1] + p2[1]*2) / 3)

    rad60 = math.radians(60)
    sin60 = math.sin(rad60)
    cos60 = math.cos(rad60)

    ux = (t[0]-s[0])*cos60 - (t[1]-s[1])*sin60 + s[0]
    uy = (t[0]-s[0])*sin60 + (t[1]-s[1])*cos60 + s[1]
    u = (ux, uy)

    kock(n-1, p1, s)
    print(*s)
    kock(n-1, s, u)
    print(*u)
    kock(n-1, u, t)
    print(*t)
    kock(n-1, t, p2)


n = int(input())
p1 = (0, 0)
p2 = (100, 0)
print(*p1)
kock(n , p1, p2)
print(*p2)
