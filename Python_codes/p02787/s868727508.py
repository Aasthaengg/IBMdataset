h,n = map(int,input().split())
magic = [ list(map(int,input().split())) for i in range(n)]
INF = float("inf")

dp =  [[INF]*(h+1) for i in range(n+1)]

"""
i番目までの魔法の中から攻撃力の合計が
jを超えるように選んだときの消費精神力の最小値
"""

for i in range(n):
    for j in range(h):
        if j < magic[i][0]:#その魔法で一撃
             dp[i+1][j+1] = min(dp[i][j+1],magic[i][1])
        elif j >= magic[i][0] and 0<= j+1-magic[i][0] <= h:
            dp[i+1][j+1] = min(dp[i][j+1],dp[i][j+1-magic[i][0]]+magic[i][1],dp[i+1][j+1-magic[i][0]]+magic[i][1])#その魔法を連打したときが考慮されていない
        
print(dp[n][h])
