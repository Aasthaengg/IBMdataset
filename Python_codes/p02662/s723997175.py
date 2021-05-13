import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
mod = 998244353

"""
X = (1,2,...,N)の部分集合
Y = Xの部分集合

各i(1 ≤ i ≤ N) について、
1. XにもYにも入れる
2. Xには入れるがYには入れない
3. XにもYにも入れない

dp[i][j] = i番目までの選択をして、sum(Y)==jであるような場合の数
"""

dp = [[0 for _ in range(S + 1)]for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(S + 1):
        # YにA[i]を入れることが出来る場合（遷移元がある場合）
        # 選択肢2,3を選ぶ場合 + 選択肢1を選ぶ場合
        if j >= A[i]:
            dp[i][j] = 2 * dp[i - 1][j] + dp[i - 1][j - A[i]]
            dp[i][j] %= mod
        # 選択肢2,3を選ぶ場合(1は選べない)
        else:
            dp[i][j] = 2 * dp[i - 1][j]
            dp[i][j] %= mod

print(dp[N][S])
