def main():
    n, s = map(int, input().split())
    mod = 998244353
    a = list(map(int, input().split()))
    dp = [[0]*(s+1) for _ in range(n+1)]
    dp[0][0] = 1
    dio = dp[0]
    for i in range(1, n+1):
        ai = a[i-1]
        di = dp[i]
        for j in range(min(s+1, ai)):
            di[j] = (di[j]+2*dio[j])%mod
        for j in range(ai, s+1):
            di[j] = (di[j]+2*dio[j]+dio[j-ai])%mod
        dp[i] = di
        dio = di
    print(dp[n][s])
    
if __name__ == "__main__":
    main()