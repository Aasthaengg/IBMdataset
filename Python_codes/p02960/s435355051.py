S = input()
INF = 10 ** 9 + 7

dp = [[0 for _ in range(13)] for _ in range(len(S) + 1)]
index = 1
dp[0][0] = 1
for i in range(len(S)):
    c = S[-i - 1]
    if c == '?':
        for j in range(10):
            for k in range(13):
                dp[i + 1][(j * index + k) % 13] += dp[i][k]
                dp[i + 1][(j * index + k) % 13] %= INF
    else:
        c = int(c)
        for k in range(13):
            dp[i + 1][(c * index + k) % 13] += dp[i][k]
            dp[i + 1][(c * index + k) % 13] %= INF
    index *= 10
    index %= 13

print(dp[len(S)][5])