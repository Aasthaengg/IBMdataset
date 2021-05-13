H, W = map(int, input().split())
a = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

mod = 10**9+7

for w in range(1, W):
    if a[0][w]=='#': break
    dp[0][w] = 1
for h in range(1, H):
    if a[h][0]=='#': break
    dp[h][0] = 1
for h in range(1, H):
    for w in range(1, W):
        if a[h][w]=='#': continue
        dp[h][w] = (dp[h-1][w]+dp[h][w-1])%mod
print(dp[-1][-1])