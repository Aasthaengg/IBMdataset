def main():
    MOD = 10**9 + 7
    S = input()
    N = len(S)
    dp = [[0 for _ in range(13)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i, c in enumerate(S):
        for j in range(10):
            if c != '?' and c != str(j):
                continue
            for k in range(13):
                dp[i + 1][(10 * k + j) % 13] += dp[i][k]
        for k in range(13):
            dp[i + 1][k] %= MOD
    print(dp[N][5])


if __name__ == '__main__':
    main()
