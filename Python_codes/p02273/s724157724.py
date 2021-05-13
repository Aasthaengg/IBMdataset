import math
n = int(input())


def koch(n, p1, p2):
    if n == 0:
        return
    s, t, u = [0, 0], [0, 0], [0, 0]
    s[0], s[1] = (2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3
    t[0], t[1] = (p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3
    u[0] = (t[1] - s[1]) * math.sin(math.radians(60)) + (t[0] - s[0]) * math.cos(math.radians(60)) + s[0]
    u[1] = (t[1] - s[1]) * math.cos(math.radians(60)) - (t[0] - s[0]) * math.sin(math.radians(60)) + s[1]

    koch(n - 1, p1, s)
    print('{:.8f}'.format(s[1]), '{:.8f}'.format(s[0]))
    koch(n - 1, s, u)
    print('{:.8f}'.format(u[1]), '{:.8f}'.format(u[0]))
    koch(n - 1, u, t)
    print('{:.8f}'.format(t[1]), '{:.8f}'.format(t[0]))
    koch(n - 1, t, p2)


p1 = [0, 0]
p2 = [0, 100]
print('{:.8f}'.format(p1[1]), '{:.8f}'.format(p1[0]))
koch(n, p1, p2)
print('{:.8f}'.format(p2[1]), '{:.8f}'.format(p2[0]))

