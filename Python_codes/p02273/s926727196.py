# -*- coding:utf-8 -*-
import math


def koch(n, p1, p2):
    if n == 0:
        return

    sx = (2 * p1[0] + 1 * p2[0]) / 3
    sy = (2 * p1[1] + 1 * p2[1]) / 3
    s = (sx, sy)

    tx = (1 * p1[0] + 2 * p2[0]) / 3
    ty = (1 * p1[1] + 2 * p2[1]) / 3
    t = (tx, ty)

    rad60 = math.radians(60)
    ux = (tx - sx) * math.cos(rad60) - (ty - sy) * math.sin(rad60) + sx
    uy = (tx - sx) * math.sin(rad60) + (ty - sy) * math.cos(rad60) + sy
    u = (ux, uy)

    koch(n - 1, p1, s)
    print(s[0], s[1])

    koch(n - 1, s, u)
    print(u[0], u[1])

    koch(n - 1, u, t)
    print(t[0], t[1])

    koch(n - 1, t, p2)


if __name__ == "__main__":
    n = int(input())
    p1 = (0.0, 0.0)
    p2 = (100.0, 0.0)
    print(p1[0], p1[1])
    koch(n, p1, p2)
    print(p2[0], p2[1])