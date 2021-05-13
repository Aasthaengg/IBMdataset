MOD = 10**9 + 7
def main():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    dp = [[0]*(m+1) for _ in range(n+1)]
    for si in range(1, n+1):
        for ti in range(1, m+1):
            if s[si-1] == t[ti-1]:
                dp[si][ti] += 1
                dp[si][ti] += dp[si-1][ti-1]
            dp[si][ti] += dp[si-1][ti] + dp[si][ti-1]
            dp[si][ti] -= dp[si-1][ti-1]
            dp[si][ti] %= MOD
    print(dp[n][m] + 1)
#    for i in range(n+1):
#        print(dp[i])

if __name__ == "__main__":
    main()
