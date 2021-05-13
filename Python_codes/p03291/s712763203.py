S = input()
dp = [[1, 0, 0, 0] for _ in range(len(S))]
if S[0] == 'A':
    dp[0][1] = 1
if S[0] == '?':
    dp[0][1] = 1
    dp[0][0] *= 3

for i, v in enumerate(S):
    if i == 0:
        continue
    if v == '?':
        dp[i][0] = dp[i-1][0] * 3 % 1000000007
        dp[i][1] = (dp[i-1][1] * 3 + dp[i-1][0]) % 1000000007
        dp[i][2] = (dp[i-1][2] * 3 + dp[i-1][1]) % 1000000007
        dp[i][3] = (dp[i-1][3] * 3 + dp[i-1][2]) % 1000000007
        continue

    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-1][2]
    dp[i][3] = dp[i-1][3]
    if v == 'A':
        dp[i][1] += dp[i-1][0]
        dp[i][1] %= 1000000007
    if v == 'B':
        dp[i][2] += dp[i-1][1]
        dp[i][2] %= 1000000007
    if v == 'C':
        dp[i][3] += dp[i-1][2]
        dp[i][3] %= 1000000007

print(dp[-1][3])