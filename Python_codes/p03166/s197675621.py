from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [[]for _ in range(n)]
dinp = [0]*n
for _ in range(m):
    x, y = list(map(lambda x: int(x)-1, input().split()))
    edges[x].append(y)
    dinp[y] += 1

queue = deque([])
for i in range(n):
    if dinp[i] == 0:
        queue.append(i)

toposorted = []
while queue:
    v = queue.popleft()
    toposorted.append(v)
    for v2 in edges[v]:
        dinp[v2] -= 1
        if dinp[v2] == 0:
            queue.append(v2)

dist = [0]*n
for i in range(n):
    v = toposorted[i]
    for v2 in edges[v]:
        if dist[v2] <= dist[v]-1:
            continue
        dist[v2] = dist[v]-1
print(-min(dist))
