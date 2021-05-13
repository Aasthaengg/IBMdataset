N,M,L = map(int,input().split())
INF = 10**13
D = [[INF]*N for _ in range(N)]
for i in range(N):
    D[i][i] = 0

for _ in range(M):
    A,B,C = map(int,input().split())
    D[A-1][B-1] = C
    D[B-1][A-1] = C

for k in range(N):
    for i in range(N-1):
        for j in range(i+1,N):
            D[i][j] = min(D[i][j],D[i][k]+D[j][k])
            D[j][i] = D[i][j]

F = [[INF]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            F[i][j] = 0
        elif D[i][j] <= L:
            F[i][j] = 1

for k in range(N):
    for i in range(N-1):
        for j in range(i+1,N):
            F[i][j] = min(F[i][j],F[i][k]+F[j][k])
            F[j][i] = F[i][j]

for i in range(N):
    for j in range(N):
        if F[i][j] == INF:
            F[i][j] = -1
        elif i != j:
            F[i][j] -= 1

Q = int(input())
for i in range(Q):
    s,t = map(int,input().split())
    print(F[s-1][t-1])

