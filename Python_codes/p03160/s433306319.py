n = int(input())
h = list(map(int,input().split()))

dp = [float("inf")]*n
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(1,n-1):
    dp[i+1] = min(dp[i]+abs(h[i+1]-h[i]),dp[i-1]+abs(h[i+1]-h[i-1]))
print(dp[n-1])