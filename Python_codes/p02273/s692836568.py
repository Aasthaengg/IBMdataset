def rev(s, t):
    xa, ya = s
    xb, yb = t
    X = xb - xa
    Y = yb - ya

    return (X - (3 ** 0.5) * Y) / 2 + xa, (Y + (3 ** 0.5) * X) / 2 + ya


def f(n):
    print(0, 0)
    _f((0, 0), (100, 0), 0, n - 1)
    print(100, 0)


def _f(p1, p2, n, end):

    if n > end:
        return
    xa, ya = p1
    xb, yb = p2
    s = xa + (xb - xa) / 3, ya + (yb - ya) / 3
    t = xa + (xb - xa) * 2 / 3, ya + (yb - ya) * 2 / 3
    u = rev(s, t)
    _f(p1, s, n + 1, end)
    print(s[0], s[1])
    _f(s, u, n + 1, end)
    print(u[0], u[1])
    _f(u, t, n + 1, end)
    print(t[0], t[1])
    _f(t, p2, n + 1, end)


def main():
    f(int(input()))


if __name__ == '__main__':
    main()

