# B - Frog 2
N,K = map(int,input().split())
h = list(map(int,input().split()))

# 無限大の値
INF = 10**10

# DP テーブル
dp = [0]*(100010)

# DP テーブル全体を初期化
for i in range(100010):
    dp[i] = INF 

# 初期条件
dp[0] = 0

for v in range(1,N):
    for k in range(1,K+1):
        # 遷移元の足場がないとき
        if v-k < 0:
            continue
        # 足場 v-k から足場 v に移動する
        dp[v] = min(dp[v], dp[v-k] + abs(h[v]-h[v-k]))
print(dp[N-1])