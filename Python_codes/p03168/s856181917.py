import numpy as np

N = int(input())
p = [0] + list(map(float, input().split()))

dp = np.zeros((3100, 3100))
#dp[i, j] = i枚目までのコインを投げて，表の個数がj枚である確率
#pythonのlistだと遅いので，numpyにおけるベクトル漸化式としてdpを埋めていく

dp[1, 0] = 1-p[1]
dp[1, 1] = p[1]

for i in range(2, N + 1):
    dp[i] = np.roll(dp[i-1], 1) * p[i] + dp[i-1] * (1-p[i])
    #dp[i][j] = i-1枚目までで表がj-1かつi回目で表　＋　i-1回目までで表がj枚かつi回目で裏（MECE）
    #つまり，dp[i][j] = dp[i-1][j-1] * p[i] + dp[i-1][j] * (1 - p[i])
    #numpyを使ってベクトル漸化式と見ることで，for_loopを一層分解消。
    #print(i, j, dp[i][j])

ans = 0

for k in range(-(-N//2), N+1):
    ans += dp[N, k]

print(ans)