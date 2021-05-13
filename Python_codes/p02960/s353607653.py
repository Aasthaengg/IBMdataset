s = input()
keta = len(s)
mod = 10 ** 9 + 7
dp = [[0] * (13) for _ in range(keta + 1)]
dp[0][0] = 1
for i in range(keta):
    if s[i] == "?":
        num = -1
    else:
        num = int(s[i])
    ni = i + 1
    juu = pow(10, keta - 1 - i, 13)
    for j in range(13):
        nj = j
        if num == -1:
            for d in range(10):
                nj = j + d * juu
                nj %= 13
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= mod
                continue
        else:
            nj = j + num * juu
            nj %= 13
            dp[ni][nj] += dp[i][j]
            dp[ni][nj] %= mod
print(dp[keta][5])
