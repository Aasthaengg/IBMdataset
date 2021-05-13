N,K = map(int,input().split())
H = list(map(int,input().split()))

INF = 10 ** 9 + 1
dp = [INF] * N
dp[0] = 0

for i in range(1, N):
  dp[i] = min(pre + abs(h - H[i]) for pre,h in zip(dp[max(0,i - K):i],H[max(0,i - K):i]))

print(dp[-1])