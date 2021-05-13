from math import cos, sin, radians
def koch(n, a, b):
        if n == 0:
                return
        s = [0, 0]
        t = [0, 0]
        u = [0, 0]
        s[0] = (2 * a[0] + 1 * b[0]) / 3
        s[1] = (2 * a[1] + 1 * b[1]) / 3
        t[0] = (1 * a[0] + 2 * b[0]) / 3
        t[1] = (1 * a[1] + 2 * b[1]) / 3
        u[0] = (t[0] - s[0]) * cos(radians(60)) - (t[1] - s[1]) * sin(radians(60)) + s[0]
        u[1] = (t[0] - s[0]) * sin(radians(60)) + (t[1] - s[1]) * cos(radians(60)) + s[1]
        koch(n - 1, a, s)
        print('{:.08f} {:.08f}'.format(s[0], s[1]))
        koch(n - 1, s, u)
        print('{:.08f} {:.08f}'.format(u[0], u[1]))
        koch(n - 1, u, t)
        print('{:.08f} {:.08f}'.format(t[0], t[1]))
        koch(n - 1, t, b)

a = [0, 0]
b = [100, 0]
n = int(input())
print('{:.08f} {:.08f}'.format(a[0], a[1]))
koch(n, a, b)
print('{:.08f} {:.08f}'.format(b[0], b[1]))

