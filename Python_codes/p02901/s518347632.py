N, M = map(int, input().split())

INF = 10**9
dp = [INF]*(1<<N)
dp[0] = 0

for _ in range(M):
  a, b = map(int, input().split())
  c = sum(map(lambda x: 1 << (int(x)-1), input().split()))
  for j in range(1<<N):
    dp[j|c] = min(dp[j|c], dp[j] + a)

ans = dp[-1]

if ans == INF:
  print(-1)
else:
  print(ans)