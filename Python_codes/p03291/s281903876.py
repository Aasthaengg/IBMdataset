S = input()

dp = [[0]*(len(S)+1) for i in range(4)]
dp[0][0] = 1

for i in range(4):
    for j in range(1, len(S)+1):
        if S[j-1] == '?':
            dp[i][j] = 3 * dp[i][j-1]
        else:
            dp[i][j] = dp[i][j-1]
        if i > 0:
            if S[j-1] == '?' or 'ABC'.find(S[j-1]) == i-1:
                dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= 10**9+7

print(dp[3][len(S)])