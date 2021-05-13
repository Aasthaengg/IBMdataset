import math


def koch(d, p1, p2):
    if d == 0:
        return

    s, t, u = [0, 0], [0, 0], [0, 0]
    s[0] = (2 * p1[0] + 1 * p2[0]) / 3
    s[1] = (2 * p1[1] + 1 * p2[1]) / 3
    t[0] = (1 * p1[0] + 2 * p2[0]) / 3
    t[1] = (1 * p1[1] + 2 * p2[1]) / 3
    u[0] = (t[0] - s[0]) * math.cos(th) - (t[1] - s[1]) * math.sin(th) + s[0]
    u[1] = (t[0] - s[0]) * math.sin(th) + (t[1] - s[1]) * math.cos(th) + s[1]

    koch(d-1, p1, s)
    print(" ".join(map(str, s)))
    koch(d-1, s, u)
    print(" ".join(map(str, u)))
    koch(d-1, u, t)
    print(" ".join(map(str, t)))
    koch(d-1, t, p2)

if __name__ == "__main__":
    th = math.radians(60)
    n = int(input())
    a = [0, 0]
    b = [100, 0]

    print(" ".join(map(str, a)))
    koch(n, a, b)
    print(" ".join(map(str, b)))