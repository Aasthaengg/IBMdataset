n = int(input())
dp = [i for i in range(n+1)]

for i in range(n):
    dp[i+1] = min(dp[i+1],dp[i] + 1)
    cou = 1
    while True:
        if i + 6**cou <= n:
            dp[i+6**cou] = min(dp[i+6**cou],dp[i]+1)
            cou += 1
        elif i + 6**cou > n:
            break
    cou = 1
    while True:
        if i + 9**cou <= n:
            dp[i+9**cou] = min(dp[i+9**cou],dp[i]+1)
            cou += 1
        elif i + 9**cou > n:
            break
print(dp[n])