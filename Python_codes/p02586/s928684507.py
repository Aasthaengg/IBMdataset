def solve():
    R,C,K = map(int, input().split())
    #value = [[0 for _ in range(C)] for _ in range(R)]
    dp = [[[0 for _ in range(C+1)] for _ in range (R+1)] for _ in range(5)]
    for _ in range(K):
        r,c,v = map(int, input().split())
        dp[4][r][c] = v

    #print(value)
    #print(dp)

    for r in range(1, R+1):
        for c in range(1, C+1):
            v = dp[4][r][c]
            prow = max(dp[0][r-1][c], dp[1][r-1][c], dp[2][r-1][c], dp[3][r-1][c])
            if v == 0: # no item
                dp[0][r][c] = max(prow, dp[0][r][c-1])
                dp[1][r][c] = dp[1][r][c-1]
                dp[2][r][c] = dp[2][r][c-1]
                dp[3][r][c] = dp[3][r][c-1]
            else:
                dp[0][r][c] = max(prow, dp[0][r][c-1])
                dp[1][r][c] = max(dp[1][r][c-1], dp[0][r][c-1] + v, prow + v)
                dp[2][r][c] = max(dp[2][r][c-1], dp[1][r][c-1] + v)
                dp[3][r][c] = max(dp[3][r][c-1], dp[2][r][c-1] + v)

    #print(dp)
    print(max(dp[0][R][C], dp[1][R][C], dp[2][R][C], dp[3][R][C]))

solve()