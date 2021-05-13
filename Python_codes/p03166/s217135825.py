import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
edges = [[]for _ in range(n)]
for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    edges[x].append(y)


def dfs(v, parent):
    if visited[v]:
        return
    visited[v] = 1
    for v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, v)
        if dist[v] >= dist[v2]+1:
            continue
        dist[v] = dist[v2]+1


dist = [0]*n
visited = [0]*n

for i in range(n):
    if visited[i]:
        continue
    dfs(i, -1)

print(max(dist))
