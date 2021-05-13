MOD = 10 ** 9 + 7


def add(x, y):
    ret = x + y
    if ret >= MOD:
        ret -= MOD
    return ret


S = input().strip()

dp = [[0] * 4 for _ in range(len(S) + 1)]
dp[0][0] = 1

for i in range(len(S)):
    unit = 3 if S[i] == '?' else 1
    for j in range(4):
        dp[i + 1][j] = dp[i][j] * unit % MOD

    if S[i] == 'A' or S[i] == '?':
        dp[i + 1][1] = add(dp[i + 1][1], dp[i][0])
    if S[i] == 'B' or S[i] == '?':
        dp[i + 1][2] = add(dp[i + 1][2], dp[i][1])
    if S[i] == 'C' or S[i] == '?':
        dp[i + 1][3] = add(dp[i + 1][3], dp[i][2])

print(dp[-1][3])