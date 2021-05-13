def YesNo(b):
    print("Yes" if b else "No")


def solve(l, t0, t):
    s = {t0}
    for v in l:
        s, ps = set(), s
        for a in ps:
            s.add(a+v)
            s.add(a-v)
    return t in s


s = input()
x, y = map(int, input().split())

f = s.split('T')
x0 = len(f[0])
xl = [len(v) for v in f[2::2]]
yl = [len(v) for v in f[1::2]]

YesNo(solve(xl, x0, x) and solve(yl, 0, y))