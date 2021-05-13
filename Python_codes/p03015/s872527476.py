l = input()
mod = 10**9 + 7

len_l = len(l)
dp = [[0] * 2 for _ in range(len_l + 1)]

dp[0][1] = 1

for i in range(1,len_l+1):
    dp[i][0] += dp[i-1][0] * 3

    if(l[i-1] == '0'):
        dp[i][1] += dp[i-1][1]
    else:
        dp[i][0] += dp[i-1][1]
        dp[i][1] += dp[i-1][1] * 2

    dp[i][0] %= mod
    dp[i][1] %= mod

ans = sum(dp[-1]) % mod
print(ans)