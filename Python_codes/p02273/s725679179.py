import math

def koch(p1, p2, n):
    if n == 0:
        return

    s = ((2 * p1[0] + 1 * p2[0]) / 3, (2 * p1[1] + 1 * p2[1]) / 3)
    t = ((1 * p1[0] + 2 * p2[0]) / 3, (1 * p1[1] + 2 * p2[1]) / 3)
    u = ((t[0] - s[0]) * math.cos(math.radians(60)) - (t[1] - s[1]) * math.sin(math.radians(60)) + s[0],
         (t[0] - s[0]) * math.sin(math.radians(60)) + (t[1] - s[1]) * math.cos(math.radians(60)) + s[1])


    koch(p1, s, n-1)
    print('{:8f} {:8f}'.format(s[0], s[1]))
    koch(s, u, n-1)
    print('{:8f} {:8f}'.format(u[0], u[1]))
    koch(u, t, n-1)
    print('{:8f} {:8f}'.format(t[0], t[1]))
    koch(t, p2, n-1)


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline # faster input

    n = int(input())

    a = (0, 0)
    b = (100, 0)

    print('{:8f} {:8f}'.format(a[0], a[1]))
    koch(a, b, n)
    print('{:8f} {:8f}'.format(b[0], b[1]))

