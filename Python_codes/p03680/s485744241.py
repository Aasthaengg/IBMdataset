n = int(input())
A = [int(input()) for _ in range(n)]

g = [[] for _ in range(n)]
for i, a in enumerate(A):
    g[a-1].append(i)

from collections import deque
q = deque([1])
visit = [-1]*n
visit[1] = 0
while q:
    v = q.popleft()
    for u in g[v]:
        if visit[u] == -1:
            visit[u] = visit[v]+1
            q.append(u)
if visit[0] == -1:
    print(-1)
else:
    print(visit[0])
