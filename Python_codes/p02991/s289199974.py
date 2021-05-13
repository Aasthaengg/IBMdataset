import sys
input = sys.stdin.buffer.readline

n, m = map(int, input().split())
g = [[] for _ in range(3*n)]
for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    g[u].append(v+n)
    g[u+n].append(v+2*n)
    g[u+2*n].append(v)
s, t = map(int, input().split())
s, t = s-1, t-1

from collections import deque
q = deque()
visit = [-1]*(3*n)
q.append(s)
visit[s] = 0
while q:
    u = q.popleft()
    for v in g[u]:
        if visit[v] == -1:
            visit[v] = visit[u]+1
            q.append(v)
if visit[t] == -1:
    print(-1)
else:
    print(visit[t]//3)
