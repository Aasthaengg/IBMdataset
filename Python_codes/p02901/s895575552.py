n, m = map(int, input().split())

dp = [[10**10 for _ in range(2**n)] for j in range(m)]
dp[0][0] = 0
a, b = map(int, input().split())
c = list(map(int, input().split()))
idx = 0
for cc in c:
  idx += 2**(cc-1)
for j in range(1, 2**n):
  if ~idx & j == 0:
    dp[0][j] = a

for i in range(1, m):
  a, b = map(int, input().split())
  c = list(map(int, input().split()))
  idx = 0
  for cc in c:
    idx += 2**(cc-1)
  for j in range(2**n):
    dp[i][j] = min(dp[i-1][j], dp[i-1][(j|idx)^idx]+a)

if dp[-1][-1] != 10**10:
  print(dp[-1][-1])
else:
  print(-1)