from math import sqrt


def func(N, p1, p2):
    if N == 0:
        return 0
    s = ((2*p1[0]+p2[0])/3, (2*p1[1]+p2[1])/3)
    t = ((p1[0]+2*p2[0])/3, (p1[1]+2*p2[1])/3)
    x = (t[0]-s[0])/2-sqrt(3)*(t[1]-s[1])/2+s[0]
    y = sqrt(3)*(t[0]-s[0])/2+(t[1]-s[1])/2+s[1]
    u = (x, y)
    func(N-1, p1, s)
    print(*s)
    func(N-1, s, u)
    print(*u)
    func(N-1, u, t)
    print(*t)
    func(N-1, t, p2)


N = int(input())
print(*(0.0, 0.0))
func(N, (0.0, 0.0), (100.0, 0.0))
print(*(100.0, 0.0))

