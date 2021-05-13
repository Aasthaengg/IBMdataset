N,Q = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

counter = [0]*N
for i in range(Q):
    p,x = map(int,input().split())
    counter[p-1] += x

from collections import deque
visited = [-1]*N
q = deque()
q.append(0)

while q:
    cur = q.popleft()
    visited[cur] = 0
    for nx in G[cur]:
        if visited[nx] != -1: continue
        counter[nx] += counter[cur]
        q.append(nx)

print(*counter)





