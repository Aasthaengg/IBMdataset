N, M = map(int, input().split())
ls = []
dp = [float('inf')]*(1<<N)
for i in range(M):
  a, b = map(int, input().split())
  c = ['0']*N
  inf = [int(i)-1 for i in input().split()]
  for i in range(b):
    x = inf[i]
    c[x] = '1'
  m = ''.join(c)
  m = int(m,2)
  ls += [(a,m)]
  dp[m] = min(a,dp[m])
dp[0] = 0
for i in range(1<<N):
  for j in range(1<<N):
    dp[i|j] = min(dp[i|j], dp[i]+dp[j])
ans = dp[-1] if dp[-1]!=float('inf') else -1
print(ans)
