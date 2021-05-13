import math

n = int(input())
theta = math.pi / 3
p1 = [0, 0]
p2 = [100, 0]


def kock(d, p1, p2):
    if d == 0:
        return

    sx = (2*p1[0] + p2[0]) / 3
    tx = (p1[0] + 2 * p2[0]) / 3
    sy = (2 * p1[1] + p2[1]) / 3
    ty = (p1[1] + 2 * p2[1]) / 3
    s = [sx, sy]
    t = [tx, ty]

    ux = (t[0] - s[0]) * math.cos(theta) - (t[1] - s[1]) * math.sin(theta) + sx
    uy = (t[1] - s[1]) * math.cos(theta) + (t[0] - s[0]) * math.sin(theta) + sy
    u = [ux, uy]

    kock(d - 1, p1, s)
    print("{0:.8f} {1:.8f}".format(*s))
    kock(d - 1, s, u)
    print("{0:.8f} {1:.8f}".format(*u))
    kock(d -1 ,u, t)
    print("{0:.08f} {1:.8f}".format(*t))
    kock(d - 1, t, p2)

if __name__ == '__main__':
    print("0.00000000 0.00000000")
    kock(n, p1, p2)
    print("100.00000000 0.00000000")