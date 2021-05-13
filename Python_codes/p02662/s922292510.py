import sys
import math

sys.setrecursionlimit(10**7)

n, s = map(int, input().split())
a = list(map(int, input().split()))
dp = [0 for _ in range(s+1)]
dp[0] = 1
for i in range(n):
    _dp = [0 for _ in range(s+1)]
    for j in range(s+1):
        if j+a[i] <= s:
            _dp[j+a[i]] += dp[j]
            _dp[j+a[i]] %= 998244353
        _dp[j] += 2*dp[j]
        _dp[j] %= 998244353
    dp = _dp
print(dp[s])