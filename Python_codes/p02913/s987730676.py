n, s = int(input()), input()
dp = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j]:
            dp[i + 1][j + 1] = min(dp[i][j] + 1, j - i)
from itertools import chain
# max(i for i in chain.from_iterable(dp))
print(max(chain.from_iterable(dp)))
