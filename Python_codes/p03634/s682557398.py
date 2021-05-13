import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((c, b))
    edges[b].append((c, a))
INF = float('inf')


def dfs(v, parent, distance):
    dist[v] = distance
    for d, v2 in edges[v]:
        if parent == v2:
            continue
        dfs(v2, v, distance+d)


q, k = map(int, input().split())
dist = [INF]*n
dfs(k-1, -1, 0)
for _ in range(q):
    x, y = map(lambda x: int(x)-1, input().split())
    print(dist[x]+dist[y])