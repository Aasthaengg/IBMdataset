# amidaをbitで管理
MOD = 10**9+7
H,W,K = map(int,input().split())
K -= 1
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        for bit in range(1<<(W-1)):
            ok = True
            for k in range(W-2):
                if bit & (1 << k) and bit & (1 << (k+1)):
                    ok = False
            if not ok:
                continue
            nj = j
            if bit & (1<<j):
                nj = j+1
            elif j>0 and bit & (1<<(j-1)):
                nj = j-1
            dp[i+1][nj] += dp[i][j]
            dp[i+1][nj] %= MOD

print(dp[H][K]%MOD)