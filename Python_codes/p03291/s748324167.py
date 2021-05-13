import math
# N = int( input())

MOD = (10 ** 9) + 7
S = input()
dp = [ [ 0 for _ in range(4)]  for _ in range(len(S) + 1)]
dp[0][0] = 1
for i in range(len(S) ):
    if S[i] == "A":
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][1] += (dp[i][0] + dp[i][1])
        dp[i + 1][2] += (dp[i][2])
        dp[i + 1][3] += dp[i][3]
    if S[i] == "B":
        dp[i + 1][0] += dp[i][0]
        dp[i + 1][1] +=dp[i][1]
        dp[i + 1][2] +=  (dp[i][1] + dp[i][2])
        dp[i + 1][3] +=dp[i][3]

    if S[i] == "C":
        dp[i + 1][0] += (dp[i][0])
        dp[i + 1][1] += dp[i][1]
        dp[i + 1][2] += dp[i][2]
        dp[i + 1][3] += (dp[i][2] + dp[i][3])

    if S[i] == "?":
        dp[i + 1][0] +=  (dp[i][0] * 3)
        dp[i + 1][1] += (dp[i][0] + (dp[i][1]) * 3)
        dp[i + 1][2] += (dp[i][1]+ (dp[i][2]) * 3)
        dp[i + 1][3] += (dp[i][2]+ (dp[i][3]) * 3)
    for j in range(0,4):
        dp[i + 1][j] %= MOD




print(dp[-1][3] % MOD)