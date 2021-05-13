from collections import deque

n = int(input())
a = list(map(int, input().split()))

a.sort()

if a[0] >= 0:
    m = sum(a[1:]) - a[0]
    print(m)
    p = a.pop(0)
    while len(a) > 1:
        b = a.pop(0)
        print(*[p, b])
        p -= b
    b = a.pop()
    print(*[b, p])
elif a[-1] <= 0:
    m = -sum(a[:-1])+a[-1]
    print(m)
    p = a.pop(-1)
    while len(a) > 0:
        b = a.pop(0)
        print(*[p, b])
        p -= b
else:
    mi = list(filter(lambda x: x < 0, a))
    pl = list(filter(lambda x: x >= 0, a))
    m = -sum(mi) + sum(pl)
    print(m)
    lp = pl.pop(0)
    mi = deque(mi)
    while len(pl) > 0:
        b = pl.pop()
        c = mi.pop()
        print(*[c, b])
        c -= b
        mi.append(c)
    while len(mi) > 0:
        b = mi.pop()
        print(*[lp, b])
        lp -= b
