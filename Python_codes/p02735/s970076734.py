H, W = map(int, input().split())
s = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]
if s[0][0] == "#": dp[0][0] = 1
for w in range(1, W):
    dp[0][w] += dp[0][w-1]
    if s[0][w] == "#" and s[0][w-1] != "#": dp[0][w] += 1
for h in range(1, H):
    dp[h][0] += dp[h-1][0]
    if s[h][0] == "#" and s[h-1][0] != "#": dp[h][0] += 1
        
for h in range(1, H):
    for w in range(1, W):
        res0 = dp[h-1][w]
        res1 = dp[h][w-1]
        if s[h][w] == "#":
            if s[h-1][w] != "#": res0 += 1
            if s[h][w-1] != "#": res1 += 1
        dp[h][w] += min(res0, res1)
print(dp[H-1][W-1])