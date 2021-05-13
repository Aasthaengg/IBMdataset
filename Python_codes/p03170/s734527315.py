N, K = map(int, input().split())
A = tuple(map(int, input().split()))

dp = [False] * (K + 1)
for i in range(1, K + 1):
    dp[i] = not all(dp[i - x] for x in A if i - x >= 0)
print('First' if dp[K] else 'Second')
