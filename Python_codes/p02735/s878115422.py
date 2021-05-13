def solve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    INF = 10 ** 9
    dp = [[0]*(w+10) for _ in range(h+10)]
    dp[0][0] = 1 if s[0][0] == '#' else 0

    for i in range(h):
        for j in range(w):
            if not i==j==0:
                dp[i][j] = INF
            if i>0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + (1 if s[i-1][j]=='.' and s[i][j]=='#' else 0))
            if j>0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + (1 if s[i][j-1]=='.' and s[i][j]=='#' else 0))

    # for i in range(h):
    #     for j in range(w):
    #         print(dp[i][j], end=' ')
    #     print()
    print(dp[h-1][w-1])


solve()