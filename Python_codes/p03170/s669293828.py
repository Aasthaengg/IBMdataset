N, K = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
dp = ['Second' for _ in range(K + 1)]
i = 0
for i in range(min(a), K + 1):
  for j in range(N):
    if i - a[j] >= 0:
      if dp[i-a[j]] == 'Second':
        dp[i] = 'First'
print(dp[K])