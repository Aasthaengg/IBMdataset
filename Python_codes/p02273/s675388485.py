import math

n = int(input())
p1 = (0, 0)
p2 = (100, 0)
points = []

def koch(n, p, q):
    if n == 0:
        return

    x1, y1 = p
    x2, y2 = q
    sx = (2 * x1 + 1 * x2) / 3
    sy = (2 * y1 + 1 * y2) / 3
    s = (sx, sy)
    tx = (1 * x1 + 2 * x2) / 3
    ty = (1 * y1 + 2 * y2) / 3
    t = (tx, ty)
    theta = math.pi / 3
    ux = (tx - sx) * math.cos(theta) - (ty - sy) * math.sin(theta) + sx
    uy = (tx - sx) * math.sin(theta) + (ty - sy) * math.cos(theta) + sy
    u = (ux, uy)

    koch(n - 1, p, s)
    print(*s)
    koch(n - 1, s, u)
    print(*u)
    koch(n - 1, u, t)
    print(*t)
    koch(n - 1, t, q)


print(*p1)
koch(n, p1, p2)
print(*p2)

