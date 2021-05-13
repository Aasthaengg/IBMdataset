from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = {i: deque() for i in range(1, n+1)}

for i in range(n):
    u, k, *v = map(int, input().split())
    v.sort()
    for vi in v:
        graph[u].append(vi)

seen = [0]*(n+1)
queue = deque()
dist = [-1]*(n+1)
def bfs(v):
    dist[v] = 0
    seen[v] = 1
    queue.append(v)
    while queue:
        q = queue[0]
        if not graph[q]:
            queue.popleft()
            continue
        g = graph[q].popleft()
        if seen[g]:
            continue
        seen[g] = 1
        dist[g] = dist[q] + 1
        queue.append(g)

bfs(1)
for id, d in enumerate(dist):
    if id == 0:
        continue
    print(id, d)
