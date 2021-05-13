from math import cos, sin, pi

def show(p):
    print(f'{p.real:.08} {p.imag:.08}')

def rotate(p, theta):
    return p*complex(cos(theta), sin(theta))

def go(n, p1, p2):
    if n == 0:
        return
    s = (p2 - p1)/3 + p1
    t = 2*s - p1
    u = rotate(t - s, pi/3) + s
    go(n - 1, p1, s)
    show(s)
    go(n - 1, s, u)
    show(u)
    go(n - 1, u, t)
    show(t)
    go(n - 1, t, p2)


p1 = complex(0, 0)
p2 = complex(100, 0)
show(p1)
go(int(input()), p1, p2)
show(p2)
