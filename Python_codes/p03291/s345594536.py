INF = 10**9+7
s = input()
dp = [[0,0,0,0] for _ in range(len(s) + 10)]

dp[0][0] = 1

for i in range(len(s)):
    for j in range(4):
        if s[i] != '?':
            dp[i+1][j] = (dp[i+1][j]+dp[i][j]) % INF
        else:
            dp[i+1][j] = (dp[i+1][j]+dp[i][j] * 3) % INF
    if s[i] == 'A' or s[i] == '?':
        dp[i+1][1] = (dp[i+1][1]+dp[i][0]) % INF
    if s[i] == 'B' or s[i] == '?':
        dp[i+1][2] = (dp[i+1][2]+dp[i][1]) % INF
    if s[i] == 'C' or s[i] == '?':
        dp[i+1][3] = (dp[i+1][3]+dp[i][2]) % INF

print(dp[len(s)][3])        