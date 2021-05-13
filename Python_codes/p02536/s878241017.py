n,m=map(int,input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

from collections import deque

d = [None] * n
def bfs(u):
    queue = deque([u])
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
cnt=0
for i in range(n):
    if d[i] is None:
        cnt+=1
        bfs(i)
print(cnt-1)