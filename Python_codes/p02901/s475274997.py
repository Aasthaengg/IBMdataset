n,m=map(int,input().split())
INF=10**9
dp=[INF for i in range(2**n)]
dp[0]=0
for i in range(m):
    a,b=map(int,input().split())
    tmp=0
    for j in list(map(int,input().split())):
        tmp+=2**(j-1)
    dp[tmp]=min(dp[tmp],a)
for i in range(2**n):
    for j in range(2**n):
        dp[i|j]=min(dp[i]+dp[j],dp[i|j])
if dp[-1]==INF:
    print(-1)
else:
    print(dp[-1])