from collections import deque

def bfs(s=0):
    que = deque([s])
    visited = [False] * N
    visited[s] = True
    while que:
        v = que.popleft()
        for u in E[v]:
            if not visited[u]:
                par[u] = v
                visited[u] = True
                que.append(u)

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
par = [-1] * N
bfs()
cnt = len([i for i in par if i == -1])
if cnt > 1:
    print('No')
else:
    print('Yes')
    for p in par[1:]:
        print(p+1)