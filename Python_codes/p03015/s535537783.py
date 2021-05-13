"""
桁DPを使う
dp[i][j][k] => 合計値のi桁目がjになるようなABの組み合わせの数。kは未満フラグ
jが1のとき、その桁ではAが1でBが0のパターンと、Aが0でBが1のパターンが考えられる。
したがってdp[i+1][1] += dp[i][j]*2という遷移となる。
jが0のとき、その桁では必ずAもBも0となる。
したがってdp[i+1][0] += dp[i][j]という遷移となる。
"""
mod = 10**9 +7
L = input()
N = len(L)
dp = [[[0]*(2) for _ in range(2)]for _ in range(N)]
dp[0][0][1] = 1
dp[0][1][0] = 2

for i in range(N-1):
    x = int(L[i+1])
    for j in range(2):
        for k in range(2):
            if k == 0:
                r = x+1
            else:
                r = 2
            for l in range(r):
                if k == 0 and l == x:
                    flag = 0
                else:
                    flag = 1
                if l == 0:
                    dp[i+1][l][flag] += dp[i][j][k]
                else:
                    dp[i+1][l][flag] += dp[i][j][k]*2
                dp[i+1][l][flag] %= mod
ans = sum(dp[-1][1])+sum(dp[-1][0])
print(ans%mod)