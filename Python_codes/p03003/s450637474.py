# ほぼ解説AC
# n,m<2000
# len(s),len(t)<100000
import sys

input = sys.stdin.buffer.readline

n, m = map(int, input().split())
mod = 10 ** 9 + 7
S = list(map(int, input().split()))
T = list(map(int, input().split()))


dp = [[0] * (m + 2) for _ in range(n + 2)]
sum_dp = [[0] * (m + 2) for _ in range(n + 2)]
# 空集合も要素とみなすのでdp[0][0]は1
dp[0][0] = 0
# i,jを見る時にi,jまでの累積和がほすぃ。
# i,jを見てi+1,j+1を決める。
for i in range(n + 1):
    for j in range(m + 1):
        # 二次元累積和の計算
        sum_dp[i][j] += dp[i][j]
        if i - 1 >= 0:
            sum_dp[i][j] += sum_dp[i - 1][j]
        if j - 1 >= 0:
            sum_dp[i][j] += sum_dp[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0:
            sum_dp[i][j] -= sum_dp[i - 1][j - 1]
        sum_dp[i][j] %= mod
        if i < n and j < m:
            # 先にsum_dp[i][j]は計算されていないとだめ。↑
            # i-1字目、j-1字目まででできるものに、新たに一致したものを加えたもの(sum_dp)と空集合(+1)
            if S[i] == T[j]:
                dp[i + 1][j + 1] = sum_dp[i][j] + 1
                dp[i + 1][j + 1] %= mod
print((sum_dp[n][m] + 1) % mod)

