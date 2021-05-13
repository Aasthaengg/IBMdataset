n, m = map(int, input().split())
C = list(map(int, input().split()))
dp = [100000] * (n + 1)
dp[0] = 0
for k in C:
    for i, t in enumerate(zip(dp[k:], dp), start = k):
        a, b = t
        dp[i] = min(a, b + 1)
print(dp[n])