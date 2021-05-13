def main():
    n, s = map(int, input().split())
    a = [int(i) for i in input().split()]
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        ai = a[i]
        for j in range(s + 1):
            if j < ai:
                dp[i + 1][j] = dp[i][j] * 2 % 998244353
            else:
                dp[i + 1][j] = (dp[i][j] * 2 + dp[i][j - ai]) % 998244353
    print(dp[n][s])

if __name__ == '__main__':
    main()