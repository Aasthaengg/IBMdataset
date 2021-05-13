from math import sin, cos, radians

N = int(input())

p1 = (0, 0)
p2 = (100, 0)
th = radians(60)

def koch(n, a, b):
    global th

    if n == 0:
        return
    
    s = ((2 * a[0] + 1 * b[0]) / 3, (2 * a[1] + 1 * b[1]) / 3)
    t = ((1 * a[0] + 2 * b[0]) / 3, (1 * a[1] + 2 * b[1]) / 3)
    u = ((t[0] - s[0]) * cos(th) - (t[1] - s[1]) * sin(th) + s[0],
         (t[0] - s[0]) * sin(th) + (t[1] - s[1]) * cos(th) + s[1])

    koch(n - 1, a, s)
    print(*s)
    koch(n - 1, s, u)
    print(*u)
    koch(n - 1, u, t)
    print(*t)
    koch(n - 1, t, b)

print(*p1)
koch(N, p1, p2)
print(*p2)
