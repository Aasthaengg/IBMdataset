n,m = map(int, input().split())
ab = []
c = []
for i in range(m):
  ab.append(list(map(int, input().split())))
  c.append(list(map(int, input().split())))
dp = [[10**18] * (2 ** n) for i in range(m+1)]
dp[0][0] = 0
for i,((a,b),c) in enumerate(zip(ab,c)):
  d = 0
  for x in c:
    d += 2 ** (x-1)
  for j in range(2**n):
    NEXT = j | d
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    dp[i+1][NEXT] = min(dp[i+1][NEXT], dp[i][j]+a)
ans = dp[m][2**n-1]
if ans == 10 ** 18:
  print(-1)
else:
  print(ans)