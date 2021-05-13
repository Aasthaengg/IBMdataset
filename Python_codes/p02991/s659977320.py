N, M = map(int, input().split())
E = {}
for v in range(1,N*3+1):
    E[v] = []
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v+N)
    E[u+N].append(v+2*N)
    E[u+2*N].append(v)
S, T = map(int, input().split())
dist = [-1 for _ in range(3*N)]
dist[S-1] = 0

q = []
q.append(S)
while q:
    n = q.pop(0)
    if n == T:
        break
    for t in E[n]:
        if dist[t-1] < 0:
            dist[t-1] = dist[n-1] + 1
            q.append(t)
print(-1 if dist[T-1] < 0 else dist[T-1] // 3)
