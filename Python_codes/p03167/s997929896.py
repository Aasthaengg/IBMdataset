def solve(H, W, a):
    mod = 10 ** 9 + 7

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if a[i][j] == '.':
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                    dp[i][j] %= mod
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    dp[i][j] %= mod

    return dp[H-1][W-1]


if __name__ == "__main__":
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]

    print(solve(H, W, a))
