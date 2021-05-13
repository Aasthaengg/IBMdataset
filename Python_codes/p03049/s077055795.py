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

from collections import defaultdict

n = ni()
s = nsn(n)

cnt = 0
dcnt = 0
dic = defaultdict(int)
for i in range(n):
    for j in range(len(s[i]) - 1):
        if s[i][j] == 'A' and s[i][j + 1] == 'B':
            cnt += 1
    dic['A'] += (s[i][-1] == 'A')
    dic['B'] += (s[i][0] == 'B')
    dcnt += s[i][-1] == 'A' and s[i][0] == 'B'

ans = min(dic['A'], dic['B'])
if dcnt >= 1 and max(dic['A'], dic['B']) == dcnt:
    print(ans - 1 + cnt)
else:
    print(ans + cnt)