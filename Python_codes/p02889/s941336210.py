INF=10**15
N,M,L=map(int,input().split())
d=[[INF for i in range(N)] for j in range(N)]
d1=[[INF for i in range(N)] for j in range(N)]
for i in range(N):
    d[i][i]=0
for m in range(M):
    A,B,C=map(int,input().split())
    d[A-1][B-1]=C
    d[B-1][A-1]=C

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for i in range(N):
        for j in range(N):
            if i!=j and d[i][j]<=L:
                d1[i][j]=1
                d1[j][i]=1
for k in range(N):
    for i in range(N):
        for j in range(N):
            d1[i][j]=min(d1[i][j],d1[i][k]+d1[k][j])

Q=int(input())
for _ in range(Q):
    s,t=map(int,input().split())
    dis=d1[s-1][t-1]
    if dis==INF:
        print(-1)
    else:
        print(dis-1)

