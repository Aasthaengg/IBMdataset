from bisect import bisect_left
from collections import defaultdict

N, T, *A = map(int, open(0).read().split())

inf = 10 ** 9 + 7
dp = [inf] * (N + 1)
ctr = defaultdict(int)
for i in range(N):
    idx = bisect_left(dp, A[i])
    dp[idx] = A[i]
    if idx != 0:
        ctr[A[i] - dp[0]] += 1

print(ctr[max(ctr)])
