

def submit():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    # dpで解く
    # dp[i][j] : マス(i, j)に至るまでに必要な最小flip回数
    dp = [
        [float('inf') for _ in range(w)] for _ in range(h)
    ]
    dp[0][0] = 0 if s[0][0] == "." else 1

    def update(dp, i, j, ni, nj):
        if s[ni][nj] == ".":
            dp[ni][nj] = min(dp[i][j], dp[ni][nj])
        elif s[i][j] == "#":
            dp[ni][nj] = min(dp[i][j], dp[ni][nj])
        else: # 次が黒であり、今が白である => flip必要回数が増える
            dp[ni][nj] = min(dp[i][j] + 1, dp[ni][nj])
    
    for i in range(h):
        for j in range(w):
            if i + 1 < h:
                update(dp, i, j, i + 1, j)
            if j + 1 < w:
                update(dp, i, j, i, j + 1)

    print(dp[h - 1][w - 1])


submit()