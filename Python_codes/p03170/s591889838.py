N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
m = A[0]

dp = [False] * (K+1)

for k in range(m, K+1):
  for a in A:
    if k - a < 0:
      continue
    if not dp[k-a]:
      dp[k] = True
      break

if dp[K]:
  print('First')
else:
  print('Second')