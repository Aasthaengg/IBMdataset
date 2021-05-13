N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (K + 1)

for i in range(1, K + 1):
    for j in range(N):
        if i - a[j] >= 0 and dp[i - a[j]] == 0:
            dp[i] = 1

print('First' if dp[K] else 'Second')
