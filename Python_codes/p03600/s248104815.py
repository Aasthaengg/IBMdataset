N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
b = [a[i][: ] for i in range(N)]
for k in range(N):
 for i in range(N):
  for j in range(N):
   b[i][j] = min(b[i][j], b[i][k] + b[k][j])
inf = 10 ** 10
if a == b:
 dp = [[inf] * N for _ in range(N)]
 for i in range(N):
  for j in range(N):
   mn = i
   for k in range(N):
    if k == j: continue
    if a[i][k] + a[k][j] == a[i][j]:
     if a[mn][j] > a[k][j]:
      mn = k
   if dp[mn][j] == inf:
    dp[mn][j] = a[mn][j]
   elif dp[mn][j] != a[mn][j]:
    print(-1)
    exit(0)
 for i in range(N):
  for j in range(N):
   if dp[i][j] == inf: dp[i][j] = 0
 print(sum([sum(dp[i]) for i in range(N)]) // 2)
else: print(-1)