import math

n = int(input())


def koch(d, p1, p2):
    """

    :param int d:
    :param list p1:
    :param list p2:
    :return:
    """
    if d == 0:
        return

    s, t, u = [0, 0], [0, 0], [0, 0]
    s[0] = (2*p1[0]+p2[0]) / 3
    s[1] = (2*p1[1]+p2[1]) / 3
    t[0] = (p1[0] + 2 * p2[0]) / 3
    t[1] = (p1[1]+2*p2[1]) / 3
    u[0] = (t[0]-s[0]) * math.cos(math.pi/3) - (t[1]-s[1]) * math.sin(math.pi/3) + s[0]
    u[1] = (t[0]-s[0]) * math.sin(math.pi/3) + (t[1]-s[1]) * math.cos(math.pi/3) + s[1]

    koch(d-1, p1, s)
    print(s[0], s[1])
    koch(d-1, s, u)
    print(u[0], u[1])
    koch(d-1, u, t)
    print(t[0], t[1])
    koch(d-1, t, p2)


def main():
    print(0.00000000, 0.00000000)
    koch(n, [0, 0], [100, 0])
    print(100.00000000, 0.00000000)


if __name__ == '__main__':
    main()

