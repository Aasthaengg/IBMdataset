H, W, k = map(int, input().split())
"""
dp[k][i][j]
i行目、j番目まで来た時に、k個アイテムをとったときの価値の最大値
"""
fs = [[0]*(W+1) for i in range(H+1)]
dp = [[[-1]*(W+1) for i in range(H+1)] for j in range(4)]

# 価値を受け取る
for i in range(k):
    h, w, v = map(int, input().split())
    fs[h-1][w-1] += v

# initialize
dp[0][0][0] = 0
dp[1][0][0] = fs[0][0]

for h in range(H):
    for w in range(W):
        for i in range(4):
            if i == 0:
                dp[i][h][w+1] = max(dp[0][h][w], dp[0][h][w+1])
            else:
                dp[i][h][w+1] = max(dp[i][h][w], dp[i][h][w+1], dp[i-1][h][w]+fs[h][w+1])
    for w in range(W):
        dp[0][h+1][w] = max(dp[0][h][w],dp[1][h][w],dp[2][h][w],dp[3][h][w],0)
        dp[1][h+1][w] = dp[0][h+1][w] + fs[h+1][w]

mx = 0
for i in range(4):
    mx = max(dp[i][H-1][W-1],mx)
print(mx)