

def submit():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    modp = 10 ** 9 + 7
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            dp[i][j] %= modp
            if i + 1 < h and a[i + 1][j] == ".":
                dp[i + 1][j] += dp[i][j]
            if j + 1 < w and a[i][j + 1] == ".":
                dp[i][j + 1] += dp[i][j]
    print(dp[h - 1][w - 1])


submit()
            
