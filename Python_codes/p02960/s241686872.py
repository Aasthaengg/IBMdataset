s = input()[::-1]
MOD = 10**9 + 7

dp = [[0] * 13 for _ in range(len(s))]

for i, x in enumerate(s):
    # 1, 10, 100, 1000...の剰余を順に計算し、各桁までの剰余を計算
    if i == 0:
        tmp = 1
    else:
        tmp = tmp * 10 % 13
    if x != "?":
        move = int(x) * tmp
        if i == 0:
            dp[i][move] = 1
        else:
            for j in range(13):
                dp[i][j] += dp[i - 1][(j - move + 13) % 13]
                dp[i][j] %= MOD
    else:
        for coef in range(10):
            move = coef * tmp
            if i == 0:
                dp[i][move] = 1
            else:
                for j in range(13):
                    dp[i][j] += dp[i - 1][(j - move + 13) % 13]
                    dp[i][j] %= MOD

print(dp[-1][5])