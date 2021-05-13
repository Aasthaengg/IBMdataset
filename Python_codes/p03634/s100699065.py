import sys
sys.setrecursionlimit(4100000)

N = int(input())
INF = 10 ** 14
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int,input().split())
    edges[a-1].append((b-1, c))
    edges[b-1].append((a-1, c))

Q, K = map(int,input().split())
d = [INF] * N
d[K-1] = 0

def dfs(x):
    for u, cost in edges[x]:
        if d[u] == INF:
            d[u] = d[x] + cost
            dfs(u)

dfs(K-1)

for _ in range(Q):
    x, y = map(int,input().split())
    ans = d[x-1] + d[y-1]
    print(ans)