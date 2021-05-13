def main():
    # import sys
    # readline = sys.stdin.readline
    # readlines = sys.stdin.readlines
    N, Ma, Mb = map(int, input().split())
    med = [tuple(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    M = 110
    dp = [[INF] * (M + 1) for _ in range(M + 1)]
    dp[0][0] = 0

    for a, b, c in med:
        for i in range(M, a - 1, -1):
            for j in range(M, b - 1, -1):
                here = dp[i - a][j - b]
                dp[i][j] = min(dp[i][j], here + c)

    ans = INF
    ma = Ma; mb = Mb
    while ma < M and mb < M:
        ans = min(ans, dp[ma][mb])
        ma += Ma
        mb += Mb
    
    if ans < INF:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
