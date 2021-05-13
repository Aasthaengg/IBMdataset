N = int(input())
L = [-1] * (2 * 10 ** 5 + 1)
mod = 10 ** 9 + 7

dp = [0] * (N + 1)

dp[0] = 1

for i in range(N):
    dp[i+1] += dp[i]
    color = int(input())
    if L[color] != -1 and L[color] != i:
        dp[i+1] += dp[L[color]]
    L[color] = i+1
    dp[i+1] %= mod

print(dp[N])