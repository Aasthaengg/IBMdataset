def solve():
    MOD = 10**9 + 7

    N, M = map(int, input().split())
    Ss = list(map(int, input().split()))
    Ts = list(map(int, input().split()))

    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for j in range(M+1):
        dp[0][j] = 1

    for i, S in enumerate(Ss, start=1):
        for j, T in enumerate(Ts, start=1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            if S == T:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] %= MOD

    print(dp[N][M])


solve()
