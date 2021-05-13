import sys
def main():
    input = sys.stdin.readline
    R, C, k = map(int, input().split())
    s = [[0] * (C + 1) for i in range(R + 1)]
    dp = [[[0] * (C + 1) for i in range(R + 1)] for j in range(4)]
    for i in range(k):
        r, c, v = map(int, input().split())
        s[r][c] = v
    for i in range(R):
        for j in range(C):
            m = max(dp[0][i][j + 1], dp[1][i][j + 1], dp[2][i][j + 1], dp[3][i][j + 1])
            for k in range(4):
                if k == 0:
                    dp[k][i + 1][j + 1] = max(dp[k][i + 1][j], m)
                else:
                    dp[k][i + 1][j + 1] = max(dp[k][i + 1][j], dp[k - 1][i + 1][j] + s[i + 1][j + 1])
            dp[1][i + 1][j + 1] = max(dp[1][i + 1][j + 1], s[i + 1][j + 1] + m)
    print(max(dp[0][R][C], dp[1][R][C], dp[2][R][C], dp[3][R][C]))
if __name__ == "__main__":
    main()
