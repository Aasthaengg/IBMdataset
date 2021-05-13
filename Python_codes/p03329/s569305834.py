N = int(input())

pow6 = [6**i for i in range(1,7)]
pow9 = [9**i for i in range(1,6)]

dp = [1e10 for i in range(N+1)]
dp[0] = 0

for i in range(N):
    dp[i+1] = dp[i]+1

    for x in pow6:
        if i+1 - x < 0: break
        dp[i+1] = min(dp[i+1], dp[i+1 - x]+1)
    
    for x in pow9:
        if i+1 - x < 0: break
        dp[i+1] = min(dp[i+1], dp[i+1 - x]+1)
    
print(dp[N])
