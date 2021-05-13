def main():
    import sys
    readline = sys.stdin.readline

    n = int(readline())
    *p, = (float(pi) for pi in readline().rstrip().split())

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # dp[投げた枚数][表の枚数] = 確率

    for i, pi in enumerate(p, 1):
        for j in range(i + 1):
            dp[i][j] += dp[i - 1][j] * (1 - pi) + dp[i - 1][j - 1] * pi

    ret = sum(dp[n][j] for j in reversed(range(n + 1)) if j * 2 > n)
    print(ret)


if __name__ == '__main__':
    main()
