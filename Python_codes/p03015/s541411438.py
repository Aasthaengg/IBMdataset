# 条件は a+b = a^bよりa&b=0→各ビットごとに(1,0),(0,1),(0,0)の組み合わせのみ
# 上の方から決めていく桁DPになりそう？
# 組み合わせがどれでも良ければ上の3つ、和が0なら1通り、和が1なら上記の2パタ。
# Lは2進数表記
L = input()
keta = len(L)
mod = 10 ** 9 + 7
# dp[桁数][smaller]
dp = [[0] * 2 for _ in range(keta + 2)]
dp[0][0] = 1
for i in range(keta):
    nd = int(L[i])
    for j in range(2):
        ni = i + 1
        nj = j
        if j == 1:
            dp[ni][nj] += 3 * dp[i][j]
            dp[ni][nj] %= mod
        else:
            if nd == 0:
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= mod
            else:  # nd==1
                dp[ni][nj] += 2 * dp[i][j]  # (1,0), (0,1)
                dp[ni][1] += dp[i][j]  # (0,0)
                dp[ni][nj] %= mod
ans = dp[keta][0] + dp[keta][1]
ans %= mod
print(ans)
