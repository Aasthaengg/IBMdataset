A, B = [int(_) for _ in input().split()]


def make(o, x, p):
    #文字列oが1個、xがp個
    #1列に50個まで
    lines = p // 50
    r = p % 50
    return [o * 100] + [(x + o) * 50, o * 100] * lines + [(x + o) * r +
                                                          (o + o) *
                                                          (50 - r), o * 100]


ans = make('.', '#', B - 1) + make('#', '.', A - 1)
print(len(ans), 100)
for s in ans:
    print(s)
