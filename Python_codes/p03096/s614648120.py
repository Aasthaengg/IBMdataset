n,*cc = map(int, open(0).read().split())
MOD = 10**9+7

from collections import defaultdict
d = {}
dp = defaultdict(lambda: 1)

for i,c in enumerate(cc):
    dp[i] = dp[i-1]
    if c in d:
        j = d[c]
        if i - j > 1:
            dp[i] += dp[j]
            dp[i] %= MOD
    d[c] = i

print(dp[n-1])