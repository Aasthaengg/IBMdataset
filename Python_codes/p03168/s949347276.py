def main():
    N = int(input())
    assert N % 2 == 1
    M = (N + 1) // 2
    P = list(map(float, input().split(' ')))
    dp = [[0 for _ in range(M + 1)] for _ in range(N)]
    dp[0][0] = 1 - P[0]
    dp[0][1] = P[0]
    for n in range(1, N):
        p = P[n]
        for m in range(min([n + 1, M]) + 1):
            if 1 <= m < M:
                dp[n][m] = dp[n - 1][m] * (1 - p) + dp[n - 1][m - 1] * p
            elif m == M:
                dp[n][m] = dp[n - 1][m] + dp[n - 1][m - 1] * p
            else:
                # m == 0
                dp[n][m] = dp[n - 1][m] * (1 - p)
    print(dp[-1][-1])


if __name__ == '__main__':
    main()