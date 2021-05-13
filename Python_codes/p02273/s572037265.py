from math import cos, sin, pi

n = int(input())

p1 = (0, 0)
p2 = (100, 0)
theta = pi/3


def koch(d, p1, p2):
    if d == 0:
        return None

    sx = (2*p1[0] + p2[0]) / 3
    sy = (2*p1[1] + p2[1]) / 3
    tx = (p1[0] + 2*p2[0]) / 3
    ty = (p1[1] + 2*p2[1]) / 3
    ux = (tx - sx) * cos(theta) - (ty - sy) * sin(theta) + sx
    uy = (tx - sx) * sin(theta) + (ty - sy) * cos(theta) + sy

    koch(d-1, p1, (sx, sy))
    print("{} {}".format(sx, sy))
    koch(d-1, (sx, sy), (ux, uy))
    print("{} {}".format(ux, uy))
    koch(d-1, (ux, uy), (tx, ty))
    print("{} {}".format(tx, ty))
    koch(d-1, (tx, ty), p2)


print("{} {}".format(p1[0], p1[1]))
koch(n, p1, p2)
print("{} {}".format(p2[0], p2[1]))

