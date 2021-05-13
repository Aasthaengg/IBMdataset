import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# inputを高速化する。
input = sys.stdin.readline
# 入力
vacation = int(input())
lst_happiness = [list(map(int, input().split())) for i in range(vacation)]
# DPテーブル
# 最大化問題なので0で初期化
dp = [[0 for i in range(3)] for j in range(vacation+1)]
# dpの最大値を更新するための関数
def chmax(a, b):
    if a > b:
        return a
    else:
        return b
# メモ化再帰の関数
def rec(i):
    # DPの値が既に更新されている場合はその値を返す
    for j in range(3):
        if dp[i][j] > 0:
            break
        
        # 再帰の終了条件
        if i == 0:
            dp[i][j] = 0
            break
        
        # i-1 を再帰
        res = 0
        for k in range(3):
            if j == k:
                continue
            res = chmax(res, rec(i-1)[k] + lst_happiness[i-1][k])
            # 結果をメモする
            dp[i][j] = res
    
    return dp[i]
ans = rec(vacation)
ans = max(ans)
print(ans)