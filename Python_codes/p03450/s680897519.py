import sys
sys.setrecursionlimit(10**7)

INF = 10**18
N, M = map(int, input().split())
g = [[] for _ in range(N)]
lst = [INF] * N

def dfs(v):
    for n, d in g[v]:
        if lst[n] == INF:
            lst[n] = lst[v] + d
            if not dfs(n):
                return False
        else:
            if lst[n] != lst[v] + d:
                return False
    return True

for i in range(M):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    g[l].append((r, d))
    g[r].append((l, -d))

for i in range(N):
    if lst[i] == INF:
        lst[i] = 0
        if not dfs(i):
            print('No')
            exit()

print('Yes')