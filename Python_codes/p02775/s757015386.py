n = list(map(int, input()))
dp = 0,1
for i in n:
    a = min(dp[0]+i, dp[1]+10-i)
    b = min(dp[0]+i+1, dp[1]+10-(i+1))
    dp = a, b
print(dp[0])