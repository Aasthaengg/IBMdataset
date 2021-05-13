import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

H, W, K = lr()
MOD = 10 ** 9 + 7
dp = [[0] * W for _ in range(H+1)]
dp[0][0] = 1
ladder = [[0] * 2 for _ in range(15)] #あえて多めに用意
ladder[1][0] = 1
for i in range(2, 9):
    ladder[i][0] = ladder[i-1][0] + ladder[i-1][1]
    ladder[i][1] = ladder[i-1][0]

ladder = [max(1, x+y) for x, y in ladder]

for i in range(1, H+1):
    for j in range(W):
        dp[i][j] += dp[i-1][j] * ladder[W-j-1] * ladder[j]
        if j > 0:
            dp[i][j] += dp[i-1][j-1] * ladder[W-j-1] * ladder[j-1]
        if j < W-1:
            dp[i][j] += dp[i-1][j+1] * ladder[W-j-2] * ladder[j]
        dp[i][j] %= MOD

print(dp[H][K-1] % MOD)
# 52