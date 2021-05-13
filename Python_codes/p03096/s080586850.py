import sys
input = sys.stdin.readline
n = int(input())
cs = [int(input()) for _ in range(n)]

from collections import defaultdict
prev = -1
c_comp = []
# 連続する色はまとめて良い
for c in cs:
    if prev != c:
        c_comp.append(c)
    prev = c

d = defaultdict(list)
for i,c in enumerate(c_comp):
    d[c].append(i)


dp = [0] * 220000
mod = 10**9 + 7

# 何個目まで見たか
inds = defaultdict(int)
ans = 0
dp[0] = 1
for i,c in enumerate(c_comp):
    i_prev = d[c][inds[c]-1]
    if inds[c] >= 1:
        # かぶっていないそれ以前の場合の数を足す
        dp[i+1] += dp[i] + dp[i_prev+1]
    else:
        # 前の色が無い or 異なる場合はなにもしない
        dp[i+1] = dp[i]
    dp[i+1] %= mod
    inds[c] += 1
print(dp[len(c_comp)])