N,M = map(int,input().split())
inf = float('inf')
D = [[inf]*N for _ in range(N)]
for i in range(N):
    D[i][i] = 0

edges = []
for _ in range(M):
    a,b,c = list(map(int,input().split()))
    a -= 1
    b -= 1
    D[a][b] = c
    D[b][a] = c
    edges.append([a,b,c])

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j],D[i][k] + D[k][j])
# for i in range(N):
#     print(D[i])
ans = 0
for e in edges:
    used = False
    for s in range(N):
        if D[s][e[0]] + e[2] == D[s][e[1]]:
            used = True
    if not used:
        ans += 1
print(ans)