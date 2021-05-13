import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((c, b))
    edges[b].append((c, a))
INF = float('inf')


def bfs(init_v):
    dist = [INF]*n
    dist[init_v] = 0
    tasks = deque([(0, init_v)])
    while tasks:
        d, v = tasks.popleft()
        for d2, v2 in edges[v]:
            if dist[v2] <= dist[v]+d2:
                continue
            dist[v2] = dist[v]+d2
            tasks.append((dist[v2], v2))
    return dist


q, k = map(int, input().split())
dist = bfs(k-1)
for _ in range(q):
    x, y = map(lambda x: int(x)-1, input().split())
    print(dist[x]+dist[y])