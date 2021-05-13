def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
 
N, M, L = map(int, input().split())
D1 = [[10**18]*N for _ in range(N)]
 
for i in range(N):
    D1[i][i] = 0
 
for _ in range(M):
    A, B, C = map(int, input().split())
    D1[A-1][B-1] = C
    D1[B-1][A-1] = C

warshall_floyd(D1)
D2 = [[10**18]*N for _ in range(N)]

for i in range(N):
    D2[i][i] = 0
    
for i in range(N):
    for j in range(N):
        if i!=j and D1[i][j]<=L:
            D2[i][j] = 1

warshall_floyd(D2)
Q = int(input())

for _ in range(Q):
    s, t = map(int, input().split())
    ans = D2[s-1][t-1]
    
    if ans==10**18:
        print(-1)
    else:
        print(ans-1)