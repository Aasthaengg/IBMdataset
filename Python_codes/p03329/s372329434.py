n = int(input())
pow6s = [6, 36, 216, 1296, 7776, 46656]
pow9s = [9, 81, 729, 6561, 59049]
coins = sorted([1] + pow6s + pow9s)
dp = [n+1] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(len(coins)):
    c = coins[i]
    ndp = dp[:]
    for j in range(n+1):
        if j-c >= 0:
            ndp[j] = min(dp[j], ndp[j-c] + 1)
    dp = ndp
print(dp[-1])