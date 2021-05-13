N,K = map(int, input().split())
h= list(map(int, input().split()))
INF=float('inf')
dp=[INF]*(N)
dp[0]=0
dp[1]=abs(h[0]-h[1])

for i in range(2,N):
    for k in range(1,K+1):
        dp[i]=min(dp[i-k]+abs(h[i]-h[i-k]),dp[i])
print(dp[-1])