def main():
    n = int(input())
    P = [0, ] + list(map(float, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j] * (1 - P[i]) + dp[i - 1][j - 1] * P[i]
    print(sum(dp[n][n // 2 + 1:]))


if __name__ == '__main__':
    main()
