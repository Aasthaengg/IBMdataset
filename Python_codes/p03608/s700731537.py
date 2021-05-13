# Author: cr4zjh0bp
# Created: Tue Mar 17 19:50:06 UTC 2020
import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
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

from itertools import permutations

n, m, R = na()
r = na()
abc = nan(m)
adj = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = abc[i]
    a -= 1
    b -= 1
    adj[a][b] = c
    adj[b][a] = c

dist = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        elif adj[i][j]:
            dist[i][j] = adj[i][j]

for i in range(n):
    for j in range(n):
        for k in range(n):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

ans = inf
for p in permutations(r):
    res = 0
    for i in range(R - 1):
        f, t = p[i] - 1, p[i + 1] - 1
        res += dist[f][t]
    ans = min(ans, res)

print(ans)