def main():
    s = input()
    n = len(s)
    mod = 10 ** 9 + 7
    dp = [[0 for _ in range(13)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        if s[i - 1] == "?":
            for now in range(10):
                for before in range(13):
                    ind = (now + 10 * before) % 13
                    dp[i][ind] += dp[i - 1][before]
                    dp[i][ind] %= mod
        else:
            for before in range(13):
                ind = (int(s[i - 1]) + 10 * before) % 13
                dp[i][ind] += dp[i - 1][before]
                dp[i][ind] %= mod
    print(dp[n][5])


if __name__ == '__main__':
    main()
