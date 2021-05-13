R, C, K = map(int, input().split())
points_dict = dict()
for _ in range(K):
    r, c, v = map(int, input().split())
    points_dict[r * 30000 + c] = v

dp = [[[0] * (C+1) for _ in range(R+1)] for _ in range(4)] # dp[4][R+1][C+1]
index = 0
for i in range(1, R+1):
    for j in range(1, C+1):
        #移動
        for k in range(4):
            if dp[0][i][j] < dp[k][i-1][j]:
                dp[0][i][j] = dp[k][i-1][j]
            if dp[k][i][j] < dp[k][i][j-1]:
                dp[k][i][j] = dp[k][i][j-1]
        #あれば、拾うかどうか
        if i * 30000 + j in points_dict:
            v = points_dict[i * 30000 + j]
            for k in range(3, 0, -1):
                if dp[k][i][j] < dp[k-1][i][j] + v:
                    dp[k][i][j] = dp[k-1][i][j] + v
"""
for i in range(4):
    print(i)
    print(*dp[i], sep = '\n')
"""
print(max((dp[i][R][C] for i in range(4))))
