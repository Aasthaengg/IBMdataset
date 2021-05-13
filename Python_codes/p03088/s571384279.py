N = int(input())

dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
# print(dp)

# dp[i][j][k][l]
# iは文字列の長さ
# j,k,lは最後から1,2,3文字目の文字に対応(A,G,C,Tを0,1,2,3にあてた)

# 長さ0の文字列は1通り
dp[0][3][3][3] = 1
MOD = 10**9 + 7

for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if dp[i][j][k][l] == 0: # 条件に当てはまるものがない場合はcontinue(これはなくてもok)
                    continue
                for add in range(4): # (i+1)文字目として新しく追加する文字
                    # ダメな5つの条件を捨てる
                    if add == 2 and j == 1 and k == 0:
                        continue
                    if add == 2 and j == 0 and k == 1:
                        continue
                    if add == 1 and j == 2 and k == 0:
                        continue
                    if add == 2 and j == 1 and l == 0:
                        continue
                    if add == 2 and k == 1 and l == 0:
                        continue
                    # ダメな条件を抜けたらaddをi+1番目に足した文字列の個数として数える
                    # S = ...j,k,l から S = ...j,k,l,add へ
                    dp[i+1][add][j][k] += dp[i][j][k][l]
                    dp[i+1][add][j][k] %= MOD

ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[N][j][k][l]
            ans %= MOD

print(ans)