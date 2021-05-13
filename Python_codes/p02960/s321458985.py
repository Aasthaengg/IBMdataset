




S = input()
N = len(S)
MOD = 10**9 + 7

# dp[i+1][j]: i桁目まで見たとき、j=1でSより厳密に小さく、13で割った時あまりがjになる個数
dp = [[0 for _ in range(13)] for _ in range(N+1)]
dp[0][0] = 1

"""
遷移
dp[i][j] -> dp[i+1][j+m] : i-1まで見た時あまりがkになる数字について、末尾にS[i]が追加されると、i-1までのあまりは10倍になるから、10*j+mを13で割ったあまりが新たなあまり
: S[i]が？の場合可能
dp[i][j] -> dp[i+1][k]   : S[i]もS[i-1]も？ではない

"""

for i in range(N):
    for j in range(13):
        if S[i] == "?":
            # ?に0~9がいれられる
            for num in range(10):
                dp[i+1][(10*j + num) % 13] += dp[i][j]
                dp[i+1][(10*j + num) % 13] %= MOD
        else:
            # i桁目の値は固定
            dp[i+1][(10*j + int(S[i])) % 13] += dp[i][j]
            dp[i+1][(10*j + int(S[i])) % 13] %= MOD


print(dp[-1][5])