# AtCoder Beginner Contest 153
# E - Crested Ibis vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_e
H, N, *A = map(int, open(0).read().split())
*A, = zip(*[iter(A)]*2)

INF = 1 << 30
dp = [INF]*(H+1)
dp[0] = 0
for i, (a, b) in enumerate(A):
    for h in range(H+1):
        mh = min(H, h+a)
        dp[mh] = min(dp[mh], dp[h] + b)
print(dp[H])
