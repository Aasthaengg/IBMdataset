def solve():
    N = int(input())
    Ps = list(map(float, input().split()))

    Qs = [1-P for P in Ps]

    dp = [0.0] * (N+2)
    dp[0] = 1.0
    for P, Q in zip(Ps, Qs):
        dp2 = [0.0] * (N+2)
        for j in range(N+1):
            if dp[j] == 0.0: continue
            dp2[j] += dp[j] * Q
            dp2[j+1] += dp[j] * P
        dp = dp2

    print(sum(dp[(N+1)//2:]))


solve()
