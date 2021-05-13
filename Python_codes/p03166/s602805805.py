from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dinp = [0]*n
edges = [[]for _ in range(n)]
for _ in range(m):
    x, y = list(map(lambda x: int(x)-1, input().split()))
    edges[x].append(y)
    dinp[y] += 1


next_v = deque([])
dist = [-1]*n
for i in range(n):
    if dinp[i] == 0:
        next_v.append(i)
        dist[i] = 0
ans = 0
while next_v:
    v = next_v.popleft()
    for v2 in edges[v]:
        dinp[v2] -= 1
        if dinp[v2] != 0:
            continue
        next_v.append(v2)
        if dist[v]+1 <= dist[v2]:
            continue
        dist[v2] = dist[v]+1
        ans = max(ans, dist[v2])
print(ans)
