from sys import stdin
input = stdin.readline
def main():
    R, C, K = map(int, input().split())
    items = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        items[r - 1][c - 1] = v
    dp = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(4)]
    dp[1][0][0] = items[0][0]
    for r in range(R):
        for c in range(C):
            for i in range(4):
                tmp = dp[i][r][c]
                # right
                if c != C - 1:
                    # unpick
                    dp[i][r][c + 1] = max(dp[i][r][c+1], tmp)
                    # pick
                    if i < 3:
                        dp[i+1][r][c + 1] = max(dp[i+1][r]
                                                [c + 1], tmp + items[r][c + 1])
                # down
                if r != R - 1:
                    # unpick
                    dp[0][r + 1][c] = max(dp[0][r + 1][c], tmp)
                    # pick
                    dp[1][r + 1][c] = max(dp[1][r + 1][c],
                                          tmp + items[r + 1][c])
    ans = 0
    for i in range(4):
        ans = max(ans, dp[i][-1][-1])
    print(ans)


if __name__ == "__main__":
    main()
