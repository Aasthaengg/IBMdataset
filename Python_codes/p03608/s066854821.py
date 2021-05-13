import sys
from itertools import permutations
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = [int(x) for x in input().strip().split()]
r = [int(x) for x in input().strip().split()]
G = [[float('inf')] * N for _ in range(N)]
for m in range(M):
    a, b, c = [int(x) for x in input().strip().split()]
    G[a-1][b-1] = c
    G[b-1][a-1] = c

for n in range(N):
    G[n][n] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

ans = float('inf')
for rr in permutations(r):
    ans_ = 0
    for i in range(len(rr)-1):
        ans_ += G[rr[i]-1][rr[i+1]-1]
    ans = min(ans, ans_)
print(ans)    