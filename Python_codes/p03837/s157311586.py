N,M = map(int,input().split())

A = []
B = []
C = []

for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)
    C.append(c)
inf = 10**18
dist = [[inf]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0

for i in range(M):
    dist[A[i]][B[i]] = C[i]
    dist[B[i]][A[i]] = C[i]

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
ans = 0
for i in range(M):
    if C[i] > dist[A[i]][B[i]]:
        ans += 1

print(ans)



