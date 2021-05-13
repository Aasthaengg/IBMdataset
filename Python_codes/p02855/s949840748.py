import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

sys.setrecursionlimit(10 ** 7)

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

h, w, k = na()
s = nsn(h)

ans = [[0] * w for _ in range(h)]
cur = 0
to = []
for i in range(h):
    j = 0
    cnt = 0
    while j < w:
        if s[i][j] == '#':
            cur += 1
            for l in to:
                ans[l][j] = cur
            ans[i][j] = cur
            k = j - 1
            j += 1
            while k >= 0 and ans[i][k] == 0:
                for l in to:
                    ans[l][k] = cur
                ans[i][k] = cur
                k -= 1
            while j < w and s[i][j] != '#':
                for l in to:
                    ans[l][j] = cur
                ans[i][j] = cur
                j += 1
        else:
            cnt += 1
            j += 1
    if cnt == w:
        if i == 0:
            to.append(i)
        elif len(to) != 0:
            to.append(i)
        else:
            for k in range(w):
                ans[i][k] = ans[i - 1][k]
    else:
        to = []

for i in range(h):
    print(*ans[i])