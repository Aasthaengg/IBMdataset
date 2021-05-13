H, W, K = map(int, input().split())
mod = 1000000007
K -= 1

Hikikata = [1] * (W + 10)
Hikikata[0] = 1
Hikikata[1] = 2
for i in range(2, W+1):
    Hikikata[i] = Hikikata[i-1] + Hikikata[i-2]
    Hikikata[i] %= mod

DP = [[0] * (W + 10) for _ in range(H+1)]

DP[0][K] = 1
for i in range(1, H + 1):
    for j in range(W):
        DP[i][j] = DP[i-1][j] * (Hikikata[j-1] * Hikikata[W-j-2]) % mod + DP[i-1][j-1] * (Hikikata[j-2] * Hikikata[W-j-2]) % mod + DP[i-1][j+1] * (Hikikata[j-1] * Hikikata[W-j-3]) % mod
        DP[i][j] %= mod

print(DP[H][0])
