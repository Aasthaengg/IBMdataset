INFTY = 10**5+10
N,M = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(M)]
G = {i:[] for i in range(1,N+1)}
dist = [[INFTY for _ in range(N+1)] for _ in range(N+1)]
for j in range(M):
    a,b,c = L[j]
    G[a].append(b)
    G[b].append(a)
    dist[a][b] = c
    dist[b][a] = c
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
cnt = 0
for j in range(M):
    a,b,c = L[j]
    if dist[a][b]<c:
        cnt += 1
print(cnt)