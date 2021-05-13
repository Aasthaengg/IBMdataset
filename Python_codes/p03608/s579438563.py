INF = 10**10

N,M,R = map(int,input().split())
r = list(map(int,input().split()))

dp = [[INF]*(N+1) for i in range(N+1)]
for i in range(N+1):
    dp[i][i]=0

for i in range(M):
    a,b,c=map(int,input().split())
    dp[a][b]=c
    dp[b][a]=c

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])

ans = INF
import itertools
for it in itertools.permutations(r):
    tmpans = 0
    for i in range(1,R):
        tmpans+=dp[it[i-1]][it[i]]
    ans = min(ans,tmpans)
print(ans)
