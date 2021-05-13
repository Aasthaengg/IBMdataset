# C - Vacation AC
N = int(input())
A = []
for _ in range(N):
    a,b,c = map(int,input().split())
    A.append((a,b,c))
    
# 無限大の値
INF = 10**10

# DP テーブル (値と前に選んだ活動を保持)
# a (j = 0), b (j = 1), c (j = 2)に記録
dp = [[0]*3 for _ in range(100010)]

# DP テーブル全体を初期化
for i in range(100010):
    for j in range(3):
        dp[i][j] = -INF# 最大化問題
        
# 初期条件
dp[0][0],dp[0][1],dp[0][2] = 0,0,0
        
# v 日目以前に (v 日目以前の幸福度最大値を求める)
for v in range(1,N+1):
    # v 日目の活動
    for w in range(3):
        # v-1 日目の活動
        for k in range(3):
            # 前日と活動が同じならスルー
            if w == k:
                continue
            # v 日目の情報は A[v-1] であることに注意
            dp[v][w] = max(dp[v][w], dp[v-1][k] + A[v-1][w])

# N 日目以前の幸福度最大値を出力
ans = max(dp[N])            
print(ans)