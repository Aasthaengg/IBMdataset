n,m = map(int,input().split())
coins = list(map(int,input().split()))

# 0はdummy
dp = [50001 for _ in range(50001)]
dp[0] = 0

for i in range(0,50001):
    for j in range(m):
        if i+coins[j] <= n:
            dp[i+coins[j]] = min(dp[i+coins[j]],dp[i]+1)
            
print(dp[n])
        
