def main():

    n, ma, mb = map(int, input().split())
    ABC = []
    for i in range(n):
        a, b, c = map(int, input().split())
        ABC.append((a, b, c))

    M = 401
    INF = 10**18
    dp = [[[INF]*M for i in range(M)] for j in range(n+1)]
    dp[0][0][0] = 0
    import copy
    for i in range(n):
        dp[i+1] = copy.deepcopy(dp[i])
        a, b, c = ABC[i]
        for j in range(M):
            for k in range(M):
                nj = j+a
                nk = k+b
                if 0 <= nj < M and 0 <= nk < M:
                    dp[i+1][nj][nk] = min(dp[i+1][nj][nk], dp[i][j][k]+c)

    import math
    ans = INF
    for j in range(1, M):
        for k in range(1, M):
            g = math.gcd(j, k)
            if j//g == ma and k//g == mb:
                ans = min(ans, dp[n][j][k])
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
