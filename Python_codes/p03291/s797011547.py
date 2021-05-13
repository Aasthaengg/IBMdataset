def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

S = "0" + input()
l = len(S) - 1


MOD = int(1e9) + 7
dp = makelist(l+1, 4)

def toInt(c):
    return [ord(c) - 65]

dp[0][-1] = 1

for i in range(1, l+1):
    if S[i] == 'A':
        dp[i][-1] = dp[i-1][-1]
        dp[i][0] = (dp[i-1][0] + dp[i-1][-1]) % MOD
        dp[i][1] = dp[i-1][1]
        dp[i][2] = dp[i-1][2]
    elif S[i] == 'B':
        dp[i][-1] = dp[i-1][-1]
        dp[i][0] = dp[i-1][0]
        dp[i][1] = (dp[i-1][1] + dp[i-1][0]) % MOD
        dp[i][2] = dp[i-1][2]
    elif S[i] == 'C':
        dp[i][-1] = dp[i-1][-1]
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]
        dp[i][2] = (dp[i-1][2] + dp[i-1][1]) % MOD
    elif S[i] == '?':
        dp[i][-1] = (dp[i-1][-1] * 3) % MOD
        dp[i][0] = ((dp[i-1][0] * 3) % MOD + dp[i-1][-1])  % MOD
        dp[i][1] = ((dp[i-1][1] * 3) % MOD + dp[i-1][0]) % MOD
        dp[i][2] = ((dp[i-1][2] * 3) % MOD + dp[i-1][1]) % MOD

print(dp[l][2])
