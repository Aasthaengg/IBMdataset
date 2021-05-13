H,W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[10**6]*(H*W) for _ in range(H*W)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        p = W*i+j
        if i > 0 and S[i-1][j] == ".":
            dp[p][p-W] = 1
            dp[p-W][p] = 1
        if i < H-1 and S[i+1][j] == ".":
            dp[p][p+W] = 1
            dp[p+W][p] = 1
        if j > 0 and S[i][j-1] == ".":
            dp[p][p-1] = 1
            dp[p-1][p] = 1
        if j < W-1 and S[i][j+1] == ".":
            dp[p][p+1] = 1
            dp[p+1][p] = 1

for i in range(H*W):
    dp[i][i] = 0
for k in range(H*W):
    for i in range(H*W):
        for j in range(H*W):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

ans = 0
for i in range(H*W):
    for j in range(H*W):
        if dp[i][j] == 10**6:
            continue
        ans = max(ans, dp[i][j])
            
print(ans)