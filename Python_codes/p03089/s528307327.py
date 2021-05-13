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

from collections import deque

n = ni()
a = na()

ok = True
ans = deque()

s = sum(a)
cur_n = n
while s:
    pos = 0
    flag = False
    i = n - 1
    j = cur_n - 1
    while i >= 0:
        if a[i] == 0:
            i -= 1
            continue
        if a[i] == j + 1:
            flag = True
            pos = i
            break
        j -= 1
        i -= 1

    if flag:
        ans.appendleft(a[pos])
        s -= a[pos]
        a[pos] = 0
        cur_n -= 1
    else:
        print(-1)
        exit()

print(*ans)