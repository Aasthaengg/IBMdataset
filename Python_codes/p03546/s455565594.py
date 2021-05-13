H,W = map(int,input().split())

dp = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]

"""
各数字から各数字への変更コストの最小値をわーシャルフロイドで計算する
"""

for i in range(10):
    for j in range(10):
        for k in range(9,-1,-1):
            dp[j][k] = min(dp[j][k],dp[j][i]+dp[i][k])

cost = 0
for i in range(H):
    for j in range(W):
        default = A[i][j]
        if default != -1:
            cost += dp[default][1]

print(cost)
