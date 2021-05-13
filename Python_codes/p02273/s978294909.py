from math import radians, cos, sin


def calc_koch(depth, p1, p2):
    if depth == 0:
        return

    s = ((2 * p1[0] + 1 * p2[0]) / 3.0, (2 * p1[1] + 1 * p2[1]) / 3.0)
    t = ((1 * p1[0] + 2 * p2[0]) / 3.0, (1 * p1[1] + 2 * p2[1]) / 3.0)
    ux = (t[0] - s[0]) * cos(radians(60)) - (t[1] - s[1]) * sin(radians(60)) + s[0]
    uy = (t[0] - s[0]) * sin(radians(60)) + (t[1] - s[1]) * cos(radians(60)) + s[1]
    u = (ux, uy)

    calc_koch(depth-1, p1, s)
    print('{0:.8f} {1:.8f}'.format(*s))
    calc_koch(depth-1, s, u)
    print('{0:.8f} {1:.8f}'.format(*u))
    calc_koch(depth-1, u, t)
    print('{0:.8f} {1:.8f}'.format(*t))
    calc_koch(depth-1, t, p2)


if __name__ == '__main__':
    # ??????????????\???
    depth = int(input())

    # ??????
    p1 = (0.0, 0.0)
    p2 = (100.0, 0.0)

    print('{0:.8f} {1:.8f}'.format(*p1))
    result = calc_koch(depth, p1, p2)
    print('{0:.8f} {1:.8f}'.format(*p2))