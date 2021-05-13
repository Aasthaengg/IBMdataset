N, T = map(int, input().split())
ls = []
for i in range(N):
  a, b = map(int, input().split())
  ls += [(a,b)]
ls.sort(key=lambda x:x[0])

dp = [[0]*(T) for i in range(N+1)]

for i in range(N):
  a,b = ls[i]
  for j in range(T-1, a-1, -1):
    dp[i+1][j] = max(dp[i][j], dp[i][j-a]+b)

last = [0]*N
last[-1] = ls[-1][1]
for i in range(N-2, -1, -1):
  last[i] = max(last[i+1], ls[i][1])

ans = 0

for i in range(1,N+1):
  ans = max(ans, max(dp[i-1])+last[i-1])

print(ans)
