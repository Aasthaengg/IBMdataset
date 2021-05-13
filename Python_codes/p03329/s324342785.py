N = int(input())

dp = [N] * (N + 1)
dp[0] = 0

'''
もらうDP
for i in range(1, N + 1):
    pow6 = 1
    while pow6 <= i:
        dp[i] = min(dp[i], dp[i - pow6] + 1)
        pow6 *= 6

    pow9 = 1
    while pow9 <= i:
        dp[i] = min(dp[i], dp[i - pow9] + 1)
        pow9 *= 9
'''
# 配るDP
for i in range(N):
    pow6 = 1
    while i + pow6 <= N:
        dp[i + pow6] = min(dp[i + pow6], dp[i] + 1)
        pow6 *= 6

    pow9 = 1
    while i + pow9 <= N:
        dp[i + pow9] = min(dp[i + pow9], dp[i] + 1)
        pow9 *= 9

print(dp[N])
