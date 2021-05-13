import sys
from collections import defaultdict as dd
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.buffer.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ms = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [0] * (N + 1)
for i in range(N):
  for n in nums:
    if i + ms[n] > N: continue
    if i != 0 and dp[i] == 0: continue
    dp[i + ms[n]] = max(dp[i] * 10 + n, dp[i + ms[n]])
print(dp[N])