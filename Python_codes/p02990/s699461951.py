def calc_comb(N, MOD):
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
        dp[0][i] = 1
        dp[i][1] = i
    for i in range(2, N + 1):
        for j in range(2, i + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            dp[i][j] %= MOD
    return dp


def main():
    MOD = 10**9 + 7
    N, K = list(map(int, input().split(' ')))
    # (N-K+1)_C_i * (K-1)_C_(i-1)
    comb = calc_comb(N, MOD)
    for i in range(1, K + 1):
        answer = comb[N - K + 1][i] * comb[K - 1][i - 1] % MOD
        print(answer)


if __name__ == '__main__':
    main()
