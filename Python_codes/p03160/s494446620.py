# A - Frog 1 (メモ化再帰)
import sys
sys.setrecursionlimit(10**6)

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

# メモ用の DP テーブル
dp = [0]*(100010)

# メモ用の DP テーブル全体を初期化
for i in range(100010):
    dp[i] = INF 

# 再帰関数
def rec(v):
    # DP の値が既に更新されていたらそのままリターン (メモ化の利点)
    if dp[v] < INF:
        return dp[v]
    
    # 初期条件
    if v == 0:
        return 0
    
    # i-1, i-2 を再帰
    res = INF
    
    # 1つ前の足場から遷移するとき
    res = chmin(res, rec(v-1) + abs(h[v] - h[v-1]))
    # 2つ前の足場から遷移するとき
    if v > 1:
        res = chmin(res, rec(v-2) + abs(h[v] - h[v-2]))
        
    # 結果をメモして返す
    dp[v] = res
    return res

# N-1 回遷移したときの最小値を出力
print(rec(N-1))