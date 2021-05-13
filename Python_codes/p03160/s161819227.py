# A - Frog 1

# change minimum 
def chmin(a, b):
    # a より b の方が小さいとき
    if (a > b):
        return b
    return a

# 無限大の値
INF = 10**10

N = int(input())
h = list(map(int,input().split()))

# DP テーブル
dp = [0]*(100010)

# DP テーブル全体を初期化
for i in range(100010):
    dp[i] = INF 

# 初期条件
dp[0] = 0

# ループ
for v in range(1,N):
    # 1つ前の足場から遷移するとき
    dp[v] = chmin(dp[v], dp[v-1] + abs(h[v] - h[v-1]))
    if v > 1:
        # 2つ前の足場から遷移するとき
        dp[v] = chmin(dp[v], dp[v-2] + abs(h[v] - h[v-2]))

print(dp[N-1])