
def resolve():
    MOD = 10 ** 9 + 7
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if i + 1 < H and G[i + 1][j] == ".":
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
            if j + 1 < W and G[i][j + 1] == ".":
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= MOD
    print(dp[H-1][W-1])


if __name__ == "__main__":
    resolve()
