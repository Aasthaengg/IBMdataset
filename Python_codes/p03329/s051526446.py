N = int(input())

dp = (N+1)*[N]
dp[0]=0

for i in range(0,N+1):
    j = 1
    while i+j <= N:
        dp[i+j]=min(dp[i+j],dp[i]+1)
        j *= 6
    j = 1
    while i+j <= N:
        dp[i+j]=min(dp[i+j],dp[i]+1)
        j *= 9

print(dp[N])