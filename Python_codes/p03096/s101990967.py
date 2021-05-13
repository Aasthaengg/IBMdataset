mod = 10**9+7
from collections import defaultdict
N = int(input())
C = defaultdict(list)
dp = [1] * N
for i in range(N):
    col = int(input())
    dp[i] = dp[i-1]
    if not len(C[col]) == 0:
        if not C[col][-1] + 1 == i:
            dp[i] = (dp[C[col][-1]] +dp[i])%mod
    C[col].append(i)
print(dp[N-1])