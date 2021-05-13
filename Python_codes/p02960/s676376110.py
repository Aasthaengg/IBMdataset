import sys

S = input().strip()

MOD = 10 ** 9 + 7

lens = len(S)

dp = [[0] * 13 for j in range(lens)]
if S[0] == "?":
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(S[0])] = 1

for i in range(1, lens):
    for j in range(13):
        if S[i] == "?":
            for k in range(10):
                amari = (j * 10 + k) % 13
                dp[i][amari] += dp[i - 1][j]
                dp[i][amari] %= MOD
        else:
            amari = (j * 10 + int(S[i])) % 13
            dp[i][amari] += dp[i - 1][j]
            dp[i][amari] %= MOD

print(dp[-1][5])
