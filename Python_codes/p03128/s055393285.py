N, M, *A = map(int, open(0).read().split())
ls = [0]*10
ls[1] = 2
ls[2] = 5
ls[3] = 5
ls[4] = 4
ls[5] = 5
ls[6] = 6
ls[7] = 3
ls[8] = 7
ls[9] = 6
A.sort(reverse=True)
cls = {ls[a] for a in A}
cls = sorted(list(cls))
dp = [-float('inf')]*(N+10)
dp[0] = 0
for i in range(1,N+1):
  dp[i] = max(dp[i-c]+1 for c in cls)
ans = 0
M = N
for i in range(dp[N]):
  for a in A:
    c = ls[a]
    if dp[M-c]+1 == dp[M]:
      ans += a*10**(dp[N]-1-i)
      M -= c
      break
print(ans)