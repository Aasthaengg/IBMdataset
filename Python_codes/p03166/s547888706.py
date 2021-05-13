import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = sys.stdin.readline

N, M = map(int, input().split())

lst_edge = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    lst_edge[x-1].append(y-1)

dp = [-1] * N

# rec(v) 頂点vを始点としたとき有効パスの長さの最大値
def rec(v):
    #print(dp, v)
    if dp[v] != -1:
        return dp[v] # 既に更新済み

    ans = 0
    lst_nv = lst_edge[v]
    for nv in lst_nv:
        ans = max(ans, rec(nv) + 1)
    dp[v] = ans # メモしながらリターン
    return dp[v]

ans_memo = 0
for i in range(N):
    ans_memo = max(ans_memo, rec(i))

print(ans_memo)