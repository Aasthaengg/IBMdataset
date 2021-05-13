import numpy as np

H, W = map(int, input().split())
temp = [list(input().replace("#","0").replace(".","1")) for i in range(H)]
masu = [[int(temp[i][j]) for j in range(W)] for i in range(H)]

dp = np.zeros((H, W))
if masu[0][0] == 0:
    dp[0][0] = 1

for i in range(0,H):
    for j in range(0,W):
        if i == 0:
            a = 100000
        else:
            if masu[i][j] == 0 and masu[i-1][j] == 1:
                a = dp[i-1][j] + 1
            else:
                a = dp[i-1][j]
        if j == 0:
            b = 100000
        else:
            if masu[i][j] == 0 and masu[i][j-1] == 1:
                b = dp[i][j-1] + 1
            else:
                b = dp[i][j-1]
        if a != 100000 or b != 100000:
            dp[i][j] = min([a, b])
print(int(dp[H-1][W-1]))
