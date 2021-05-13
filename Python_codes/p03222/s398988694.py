H, W, K = map(int, input().split())
MOD, p, cnt = 10**9+7, [0]*W, 0
for bit in range(1<<(W-1)):
    s0 = bit&1
    flg=True
    for w in range(1, W-1):
        if (bit>>w)&1 and s0 == 1:flg=False; break
        s0 = (bit>>w)&1
    if flg:
        cnt += 1
        for w in range(W - 1):
            if (bit >> w)&1:p[w] += 1
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        if w:
            dp[h+1][w-1] += dp[h][w]*p[w-1]
            dp[h+1][w-1] %= MOD
        if w-(W - 1):
            dp[h+1][w+1] += dp[h][w]*p[w]
            dp[h+1][w+1] %= MOD
        dp[h+1][w]+=dp[h][w]*(cnt-p[w-1]-p[w])
        dp[h+1][w]%=MOD
print(dp[H][K-1])