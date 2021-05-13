H, W, K = map(int, input().split())
Map = [[0] * (W + 1) for _ in range(H + 1)]
for _ in range(K):
    h, w, k = map(int, input().split())
    Map[h][w] = k

DP = [[[0] * (H + 1) for _ in range(W + 1)] for __ in range(4)]


for i in range(1, H + 1):
    for j in range(1, W + 1):
        x = Map[i][j]
        if Map:
            DP[0][j][i] = max(DP[0][j][i-1], DP[1][j][i-1], DP[2][j][i-1], DP[3][j][i-1], DP[0][j-1][i])
            DP[1][j][i] = max(DP[1][j - 1][i], DP[0][j-1][i] + x, DP[0][j][i-1] + x, DP[1][j][i-1] + x, DP[2][j][i-1] + x, DP[3][j][i-1] + x)
            DP[2][j][i] = max(DP[2][j - 1][i], DP[1][j-1][i] + x)
            DP[3][j][i] = max(DP[3][j - 1][i], DP[2][j-1][i] + x)

        else:
            DP[0][j][i] = max(DP[0][j][i-1], DP[1][j][i-1], DP[2][j][i-1], DP[3][j][i-1], DP[0][j-1][i])
            DP[1][j][i] = DP[1][j-1][i]
            DP[2][j][i] = DP[2][j-1][i]
            DP[3][j][i] = DP[3][j-1][i]

print(max(DP[0][W][H], DP[1][W][H], DP[2][W][H], DP[3][W][H]))