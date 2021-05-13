n = int(input())
h = [int(i) for i in input().split()]
# dpの最小値を変更する関数
def chmin(a, b):
    if a > b:
        return b
    else:
        return a
    
# 無限大の値
f_inf = float('inf')
# DP テーブルを初期化　(最小化問題なので INF に初期化)
dp = [f_inf] * (10**5+10)
# 初期条件
dp[0] = 0
# 足場 i から足場 i+1 へ移動する。コストは|h[i]−h[i+1]|
# 足場 i から足場 i+2 へと移動する コストは |h[i]−h[i+2]|
for i in range(n-1):
    dp[i + 1] = chmin(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
    # n-2の時は2つ先はない
    if i < n-2:
        dp[i + 2] = chmin(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))
print(dp[n-1])