H, W = map(int, input().split())
a = []
for _ in range(H):
    a.append(input())

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if a[i][j] == '#': 
            continue
        if i + 1 < H and a[i+1][j] == '.':
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= 1e9 + 7
        if j + 1 < W and a[i][j+1] == '.':
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= 1e9 + 7
        
print(int(dp[-1][-1]))