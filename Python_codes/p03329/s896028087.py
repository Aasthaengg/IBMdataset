N = int(input())

dp = [0] * 100001

dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    j = 1
    while 6 ** j <= i:
        dp[i] = min(dp[i], dp[i - (6 ** j)] + 1)
        j += 1
    j = 1
    while 9 ** j <= i:
        dp[i] = min(dp[i], dp[i - (9 ** j)] + 1)
        j += 1

print(dp[N])
