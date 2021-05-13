n = int(input())
mod = 10**9+7

stone = [0 for _ in range(2*10**5)]
stone_last_pos = [-1 for _ in range(2*10**5)]

dp = [0 for _ in range(n+1)]
dp[0] = dp[-1] = 1

for i in range(n):
    c = int(input())
    if i == 0:
        dp[0] = 1
    else:
        p = stone_last_pos[c-1]
        if p == i-1:
            dp[i] = dp[i-1]
        elif p > -1:
            dp[i] = dp[i-1] + dp[p]
            dp[i] %= mod
        else:
            dp[i] = dp[i-1]
    stone_last_pos[c-1] = i

print(dp[n-1])
