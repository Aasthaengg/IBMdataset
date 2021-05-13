n,m,l=map(int,input().split())
d=[[10**18]*n for i in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if c<=l:
        d[a-1][b-1]=c
        d[b-1][a-1]=c
for i in range(n):
    d[i][i]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])

for i in range(n):
    for j in range(n):
        if d[i][j]<=l:
            d[i][j]=1
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
q=int(input())
for i in range(q):
    s,t=map(int,input().split())
    s-=1
    t-=1
    print(d[s][t]-1 if d[s][t]-1<999999999999999999 else -1)


