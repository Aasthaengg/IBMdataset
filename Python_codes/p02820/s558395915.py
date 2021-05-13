def solve():
    def max2(x, y): return x if x >= y else y

    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    Ts = input().rstrip()

    Uss = [Ts[i::K] for i in range(K)]

    ans = 0
    for Us in Uss:
#        print('\nUss:', Uss)
        lenU = len(Us)
        dp = [[0]*(3) for _ in range(lenU+1)]
        for i, U in enumerate(Us, start=1):
            # グー
            dp[i][0] = max2(dp[i-1][1], dp[i-1][2])
            if U == 's':
                dp[i][0] += R
            # チョキ
            dp[i][1] = max2(dp[i-1][0], dp[i-1][2])
            if U == 'p':
                dp[i][1] += S
            # パー
            dp[i][2] = max2(dp[i-1][0], dp[i-1][1])
            if U == 'r':
                dp[i][2] += P
#            print(dp[i])

        ans += max(dp[-1])

    print(ans)


solve()
