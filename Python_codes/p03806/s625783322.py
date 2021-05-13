def main():
    n, ma, mb = map(int, input().split())
    ABC = []
    for i in range(n):
        a, b, c = map(int, input().split())
        ABC.append((a, b, c))

    INF = 10**18
    dp = [[[INF]*405 for i in range(405)] for j in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        a, b, c = ABC[i]
        for j in range(405):
            for k in range(405):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                nj, nk = j+a, k+b
                if 1 <= nj <= 404 and 1 <= nk <= 404:
                    dp[i+1][nj][nk] = min(dp[i][nj][nk], dp[i][j][k]+c)

    import fractions
    ans = INF
    for j in range(1, 405):
        for k in range(1, 405):
            if ma*k == mb*j:
                ans = min(ans, dp[n][j][k])
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
