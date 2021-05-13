def warshal(d):
    n=len(d)
    for k in range(1,n):
        for i in range(1,n):
            for j in range(1,n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
n,m,l=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]
q=int(input())
st=[list(map(int,input().split())) for i in range(q)]
inf=float("inf")
dp=[[inf]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=0
for u in abc:
    a,b,c=u
    dp[a][b]=c
    dp[b][a]=c
dp=warshal(dp)
data=[[inf]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if 0<dp[i][j]<=l:
            data[i][j]=1
        elif dp[i][j]==0:
            data[i][j]=0
data=warshal(data)
for u in st:
    s,t=u
    if data[s][t]!=inf:
        print(data[s][t]-1)
    else:
        print(-1)