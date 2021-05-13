n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a,b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

from collections import deque
q = deque([])
q.append(0)
visit = [-1]*n
visit[0] = 0
while q:
    v = q.popleft()
    for u in g[v]:
        if visit[u] == -1:
            visit[u] = v
            q.append(u)
print('Yes')
for i in range(1, n):
    print(visit[i]+1)
