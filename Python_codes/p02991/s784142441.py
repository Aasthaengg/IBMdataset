from collections import deque

N, M = map(int, input().split())
edge = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
S, T = map(int, input().split())
S, T = S-1, T-1

INF = float('inf')
dist = [[INF for i in range(3)] for j in range(N)]

def bfs():
    q = deque()
    q.append((S, 0))
    dist[S][0] = 0
    while q:
        p = q.popleft()
        v = p[0]
        l = p[1]
        for nv in edge[v]:
            nl = (l+1)%3
            if dist[nv][nl] != INF:
                continue
            dist[nv][nl] = dist[v][l] + 1
            q.append((nv, nl))
    return dist[T][0]

ans = bfs()
if ans == INF:
    ans = -1
else:
    ans = ans // 3
print(ans)