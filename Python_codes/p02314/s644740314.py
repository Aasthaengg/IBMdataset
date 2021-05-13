from itertools import product
n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [i for i in range(n+1)]
for j, k in product(range(1, m), range(1, n+1)):
    if 0 <= k - c[j]:
        dp[k] = min(dp[k], dp[k-c[j]] + 1)
print(dp[-1])
