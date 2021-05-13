N,M,Q=map(int,input().split())
x=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    L,R=map(int,input().split())
    x[L][R]+=1
for i in range(N+1):
    for j in range(N):
        x[i][j+1]+=x[i][j]
for j in range(N+1):
    for i in range(N):
        x[i+1][j]+=x[i][j]
for i in range(Q):
    p,q=map(int,input().split())
    print(x[q][q]-x[p-1][q]-x[q][p-1]+x[p-1][p-1])