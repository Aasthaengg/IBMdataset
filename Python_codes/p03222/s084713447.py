MOD = 10**9 + 7
H, W, K = map(int,input().split())
dp = [[0 for k in range(W)] for l in range(H+1)]
dp[0][0] = 1
A = []  # ありうる横棒のリスト
for b in range(2**(W-1)):
    if "11" not in bin(b):
        A.append(bin(b)[2:].zfill(W-1))

for k in range(H):
    for e in A:
        for i in range(W):
            if i < W-1 and e[i] == "1": # 右に行くパターン
                dp[k+1][i+1] += dp[k][i]
                dp[k+1][i+1] %= MOD
            elif i >= 1 and e[i-1] == "1": # 左に行くパターン
                dp[k+1][i-1] += dp[k][i]
                dp[k+1][i-1] %= MOD
            else:
                dp[k+1][i] += dp[k][i]
                dp[k+1][i] %= MOD

print(dp[H][K-1])
