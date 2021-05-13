MOD = 10**9 + 7


def main():
    L = input()
    N = len(L)
    dp = [[0]*2 for i in range(N+1)]
    dp[0][0] = 1

    for i in range(N):
        # smaller: 1 -> 1
        if L[i] == "1":
            dp[i+1][1] += dp[i][1] * 3
            dp[i+1][1] %= MOD
        else:
            dp[i+1][1] += dp[i][1] * 3
            dp[i+1][1] %= MOD
        # smaller: 0 -> 1
        if L[i] == "1":
            dp[i+1][1] += dp[i][0] * 1
            dp[i+1][1] %= MOD
        # smaller: 0 -> 0
        if L[i] == "1":
            dp[i+1][0] += dp[i][0] * 2
            dp[i+1][0] %= MOD
        else:
            dp[i+1][0] += dp[i][0] * 1
            dp[i+1][0] %= MOD

    print((dp[N][0]+dp[N][1]) % MOD)


if __name__ == '__main__':
    main()
