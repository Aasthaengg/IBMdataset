# input
H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))

# process
dp = [[100]*(W+1) for _ in range(H+1)]
dp2 = [[True]*(W+1) for _ in range(H+1)]
dp[0][1] = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            x = dp[i][j+1]+1 if dp2[i][j+1] else dp[i][j+1]
            y = dp[i+1][j]+1 if dp2[i+1][j] else dp[i+1][j]
            dp2[i+1][j+1] = False
        else:
            x = dp[i][j+1]
            y = dp[i+1][j]
            dp2[i+1][j+1] = True
        dp[i+1][j+1] = min(dp[i+1][j+1], x, y)

# output
print(dp[-1][-1])
