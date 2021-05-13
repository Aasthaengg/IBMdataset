def p_d():
    n = int(input())
    mod = 10 ** 9 + 7
    # dp[i][j][k][l]: 長さiの文字列でi-2番目がj、i-1番目がk、i番目がlであるものの総数
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == 1 and k == 2 and l == 3:
                    continue
                if j == 2 and k == 1 and l == 3:
                    continue
                if j == 1 and k == 3 and l == 2:
                    continue
                dp[3][j][k][l] = 1
    for i in range(4, n + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 1 and k == 2 and l == 3:
                            continue
                        if j == 2 and k == 1 and l == 3:
                            continue
                        if j == 1 and k == 3 and l == 2:
                            continue
                        if m == 1 and k == 2 and l == 3:
                            continue
                        if m == 1 and j == 2 and l == 3:
                            continue
                        dp[i][j][k][l] += dp[i - 1][m][j][k]
                        dp[i][j][k][l] %= mod

    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[n][j][k][l]
                ans %= mod
    print(ans)


if __name__ == '__main__':
    p_d()
