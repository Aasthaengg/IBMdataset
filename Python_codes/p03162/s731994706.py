import sys
sys.setrecursionlimit(10**6)
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
        dp[i][j] = 0# 最大化問題

def rec(v):
    # v 日目の活動
    for w in range(3):
        # DP の値がすでに更新されていたらそのままリターン
        if dp[v][w] > 0:
            return dp[v]
        # 初期条件
        if v == 0:
            dp[v][w] = 0
            return dp[v]
        # v-1 を再帰
        res = 0
        for k in range(3):
            # 前日と活動が同じならスルー
            if w == k:
                continue
            res = max(res, rec(v-1)[k] + A[v-1][w])
            # 結果をメモして返す
            dp[v][w] = res
    return dp[v]
rec(N)
ans = max(dp[N])
print(ans)