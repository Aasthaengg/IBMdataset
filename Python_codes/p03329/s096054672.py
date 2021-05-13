N = int(input())
inf = float("inf")
dp = [inf for _ in range(N+1)]
l6 = 7
l9 = 6
dp[0] = 0

# DP
for i in range(1, N+1):
    # 1円を引き出す
    dp[i] = min(dp[i], dp[i-1] + 1)
    
    # 6の累乗円を引き出す
    for j in range(1, l6):
        if i - 6**j >= 0:
            dp[i] = min(dp[i], dp[i - 6**j] + 1)
        
    # 9の累乗円を引き出す
    for j in range(1, l9):
        if i - 9**j >= 0:
            dp[i] = min(dp[i], dp[i - 9**j] + 1)

print(dp[N])