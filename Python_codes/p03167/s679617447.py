H, W = map(int, input().split())
a = [input() for _ in range(H)]

MOD = 10**9+7

dp = [[0]*W for _ in range(H)]

for i in range(H):
    if a[i][0] == '.':
        dp[i][0] = 1
    else :
        break

for j in range(W):
    if a[0][j] == '.':
        dp[0][j] = 1
    else :
        break

for i in range(H):
    for j in range(W):
        if i != 0  or j != 0:
            if a[i][j] == '#':
                dp[i][j] = 0
            else :
                dp[i][j] = (dp[i-1][j]+dp[i][j-1])%MOD
print(dp[H-1][W-1])
