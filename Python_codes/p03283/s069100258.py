import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, Q = mapint()
query = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    l, r = mapint()
    query[l][r] += 1

from itertools import accumulate
for i in range(N+1):
    query[i] = list(accumulate(query[i]))
for i in range(1, N+1):
    for j in range(N+1):
        query[i][j] += query[i-1][j]

for _ in range(Q):
    p, q = mapint()
    print(query[N][q]-query[p-1][q])