import sys

readline = sys.stdin.readline

def solve():
    R, C, K = map(int, readline().split())
    items = [[0] * C for i in range(R)]
    for i in range(K):
        r,c,k = map(int, readline().split())
        items[r - 1][c - 1] = k
    
    dp = [[[0] * C for i in range(R)] for j in range(4)]

    for i in range(R):
        for j in range(C):
            for k in range(4):
                if i == 0 and j == 0:
                    if k == 0:
                        dp[k][i][j] = 0
                    else:
                        dp[k][i][j] = items[i][j]
                elif i == 0:
                    if k == 0:
                        dp[k][i][j] = dp[k][i][j - 1]
                    else:
                        dp[k][i][j] = max(dp[k - 1][i][j - 1] + items[i][j], dp[k][i][j - 1])
                elif j == 0:
                    if k == 0:
                        dp[k][i][j] = dp[3][i - 1][j]
                    else:
                        dp[k][i][j] = dp[3][i - 1][j] + items[i][j]
                else:
                    if k == 0:
                        dp[k][i][j] = max(dp[3][i - 1][j], dp[k][i][j - 1])
                    else:
                        dp[k][i][j] = max(
                            dp[3][i - 1][j] + items[i][j],
                            dp[k - 1][i][j - 1] + items[i][j],
                            dp[k][i][j - 1]
                        )

    print(dp[-1][-1][-1])

solve()