H, W, K = map(int, input().split())
W2 = W-1
c = [0] * (W2+1)
cnt = 0
MOD = 10**9 + 7
for bit in range(1 << W2):
    s0 = bit&1
    flg=True
    for i in range(1, W2):
        if (bit>>i)&1 and s0 == 1:
            flg = False
            break
        s0 = (bit>>i)&1
    if flg:
        cnt += 1
        for i in range(W2):
            if (bit >> i)&1:
                c[i] += 1
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1
for h in range(H):
    for i in range(W):
        if i != 0:
            dp[h+1][i-1] += dp[h][i]*c[i-1]
            dp[h+1][i-1] %= MOD
        if i != W-1:
            dp[h+1][i+1] += dp[h][i]*c[i]
            dp[h+1][i+1] %= MOD
        dp[h+1][i] += dp[h][i]*(cnt-c[i-1]-c[i])
        dp[h+1][i] %= MOD
print(dp[H][K-1])