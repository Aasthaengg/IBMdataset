import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]


def gen(k, c0, c1, w):
    ww = w // 2
    w = 2 * ww
    n_rows = k // ww + 1
    remaining = k % ww
    res = []
    line = c1 * w
    for i in range(2 * n_rows):
        if i % 2 == 1:
            res.append(line)
        else:
            i //= 2
            if i != n_rows - 1:
                s = ''.join((c0 + c1) * ww)
            else:
                s = ''.join((c0 + c1) * remaining) + c1 * (w - 2 * remaining)
            res.append(s)
    return res


a, b = ril()
h, w = 100, 100
c0, c1 = '.', '#'
res = []
res += gen(a - 1, c0, c1, w)
res.append(c0 * w)
if b > 1:
    res += gen(b - 1, c1, c0, w)

print(len(res), w)
for s in res:
    print(s)