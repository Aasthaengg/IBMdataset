def main():
    # 写経AC
    MOD = 10**9 + 7
    S = input()
    N = len(S)
    dp = [[0]*2 for i in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        # a+b = 0
        if S[i] == '0':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
        else:
            dp[i+1][1] = dp[i][0] + dp[i][1]
            dp[i+1][1] %= MOD
        # a+b = 1
        if S[i] == '0':
            dp[i+1][1] += dp[i][1]*2
            dp[i+1][1] %= MOD
        else:
            dp[i+1][0] += dp[i][0]*2
            dp[i+1][0] %= MOD
            dp[i+1][1] += dp[i][1]*2
            dp[i+1][1] %= MOD
    print((dp[N][0]+dp[N][1]) % MOD)


if __name__ == '__main__':
    main()
