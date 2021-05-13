MOD = 10**9 + 7


def main():
    S = input()
    N = len(S)
    dp = [[0]*2 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        # smaller: 1 -> 1
        dp[i+1][1] += dp[i][1]*3

        # smaller: 0 -> 0
        if S[i] == "1":
            dp[i+1][0] += dp[i][0]*2
        else:
            dp[i+1][0] += dp[i][0]

        # smaller: 0 -> 1
        if S[i] == "1":
            dp[i+1][1] += dp[i][0]

        dp[i+1][0] %= MOD
        dp[i+1][1] %= MOD

    print((dp[N][0]+dp[N][1]) % MOD)


if __name__ == '__main__':
    main()
