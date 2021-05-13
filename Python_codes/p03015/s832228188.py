#129_E
l = input()
x = len(l)
mod = 10 ** 9 + 7

dp = [[0 for _ in range(2)] for _ in range(x)]
dp[0][1] = 2
dp[0][0] = 1
for i in range(1, x):
    if l[i] == '0':
        dp[i][1] = (dp[i][1] + dp[i-1][1]) % mod
    else:
        dp[i][1] = (dp[i][1] + dp[i-1][1] * 2) % mod
        dp[i][0] = (dp[i][0] + dp[i-1][1]) % mod
        
    dp[i][0] = (dp[i][0] + dp[i-1][0] * 3) % mod
print((dp[x-1][0] + dp[x-1][1]) % mod)