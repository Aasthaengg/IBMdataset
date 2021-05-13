def resolve():
    n, s = map(int, input().split())
    a = list(map(int,input().split()))
    dp = [[0]*(s+10) for _ in range(n+10)]
    dp[0][0] = 1
    mod = 998244353
    for i in range(1,n+1):
        nexta = a[i-1]
        for j in range(0, s+1):
            dp[i][j] += (2 * dp[i - 1][j])% mod
            if j + nexta > s:
                continue
            else:
                dp[i][j+nexta] += (dp[i-1][j])%mod
    print((dp[n][s])%mod)
resolve()