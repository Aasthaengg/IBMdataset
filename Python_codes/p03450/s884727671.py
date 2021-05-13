import sys

sys.setrecursionlimit(10000000)
N, M = [int(_) for _ in input().split()]

LRD = []
path = [[] for _ in range(N + 1)]
for _ in range(M):
    l, r, d = [int(_) for _ in input().split()]
    path[l].append((r, d))
    path[r].append((l, -d))
    LRD.append((l, r, d))

INF = -1e12
memo = [INF] * (N + 1)


def dfs(n):
    for ni, d in path[n]:
        if memo[ni] != INF: continue
        memo[ni] = memo[n] + d
        dfs(ni)


for i in range(1, N + 1):
    if memo[i] != INF: continue
    memo[i] = 0
    dfs(i)
for l, r, d in LRD:
    if memo[l] + d != memo[r] and memo[l] - d != memo[r]:
        print('No')
        exit()
print('Yes')
