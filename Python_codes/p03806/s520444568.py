import sys
input=sys.stdin.readline
n,ma,mb=map(int,input().split())
med=[]
for i in range(n):
    a,b,c=map(int,input().split())
    med.append((a,b,c))
INF=10000
dp=[[[INF]*401 for j in range(401)] for i in range(n+1)]
dp[0][0][0]=0
for i in range(n):
    for a in range(401):
        for b in range(401):
            if dp[i][a][b]!=INF:
                dp[i+1][a+med[i][0]][b+med[i][1]]=min(dp[i+1][a+med[i][0]][b+med[i][1]],dp[i][a][b]+med[i][2])
                dp[i+1][a][b]=min(dp[i+1][a][b],dp[i][a][b])
minc=INF
for a in range(1,401):
    for b in range(1,401):
        if a*mb==b*ma:
            minc=min(dp[n][a][b],minc)
if minc==INF:
    print(-1)
else:
    print(minc)
