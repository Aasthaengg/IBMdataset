H, W = map(int, input().split())
S = [input() for _ in range(H)]

dp = [[0]*W for _ in range(H)]
if S[0][0] == "#":
    dp[0][0] = 1

for i in range(1, W):
    if S[0][i-1] == S[0][i]:
        dp[0][i] = dp[0][i-1]
    else:
        dp[0][i] = dp[0][i-1]+1

for i in range(1, H):
    if S[i-1][0] == S[i][0]:
        dp[i][0] = dp[i-1][0]
    else:
        dp[i][0] = dp[i-1][0]+1


for i in range(1, H):
    for j in range(1, W):
        if S[i][j] == S[i-1][j]:
            a = dp[i-1][j]
        else:
            a = dp[i-1][j]+1
        if S[i][j] == S[i][j-1]:
            b = dp[i][j-1]
        else:
            b = dp[i][j-1]+1
        dp[i][j] = min(a, b)

print((dp[H-1][W-1]+1)//2)