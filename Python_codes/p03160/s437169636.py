N = int(input())
h = list(map(int, input().split()))
dp = [10**10 for _ in range(N)]
dp[0] = 0

for i in range(N-1):
    if(i+2 > N-1):
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i+1]-h[i]))
    else:         
        dp[i+2] = min(dp[i+2], dp[i]+abs(h[i+2]-h[i]))
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i+1]-h[i]))

print(dp[-1])  