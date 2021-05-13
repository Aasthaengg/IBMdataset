def w(d):
    n=len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
N,M,L = map(int, input().split())
inf=float('inf')
fuel=[[inf]*N for _ in range(N)]
for i in range(N):
    fuel[i][i]=0
for _ in range(M):
    a,b,c=map(int,input().split())
    fuel[a-1][b-1]=fuel[b-1][a-1]=c
Q=int(input())
ST=[list(map(int, input().split())) for _ in range(Q)]
fuel = w(fuel)
for i in range(N):
    for j in range(N):
        if 0 < fuel[i][j] <= L:
            fuel[i][j]=1
        elif fuel[i][j] != 0:
            fuel[i][j] = inf
fuel = w(fuel)
for st in ST:
    print(fuel[st[0]-1][st[1]-1]-1 if fuel[st[0]-1][st[1]-1] != inf else -1)
