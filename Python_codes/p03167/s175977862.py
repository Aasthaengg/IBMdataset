H, W = map(int, input().split())
a = [input() for _ in range(H)]
MOD = 10**9 + 7

dp = [[0]*1100 for _ in range(1100)]
dp[1][1] = 1
for h in range(1, H+1):
    for w in range(1, W+1):
        if h == 1 and w == 1:
            continue
        if a[h-1][w-1] == '#':
            dp[h][w] = 0
        else:
            dp[h][w] += (dp[h-1][w] + dp[h][w-1]) % MOD
print(dp[H][W] % MOD)