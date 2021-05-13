MOD = 10 ** 9 + 7
S = input()
dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1

for i in range(len(S)):
    tmpS = 0
    if S[i] == '?':
        tmpS = -1
    else:
        tmpS = int(S[i])
    for j in range(10):
        if tmpS != -1 and tmpS != j: continue
        for k in range(13):
            dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
            dp[i + 1][(k * 10 + j) % 13] %= MOD

print(dp[len(S)][5])