N,M=map(int,input().split())
lists=list(map(int,input().split()))
dp=[float("inf") for i in range(N+1)]
dp[0]=0
for i in range(1,N+1):
    for num in lists:
        if i>=num:
            dp[i]=min(dp[i],dp[i-num]+1)
print(dp[N])
