N = int(input())
A = list(map(int, input().split()))
B = [[a, i] for i, a in enumerate(A, 1)]
B.sort(reverse=True)

dp = [[0] * (N+1) for i in range(N+1)]
s, i = B[0]
dp[1][0] = s*(i - 1)
dp[0][1] = s*(N - i)
for n in range(2, N+1):
  a, i = B[n-1]
  for l in range(n+1):
    r = n - l
    if l == 0:
      dp[l][r] = dp[l][r-1] + abs(N-r+1 - i)*a
    elif r == 0:
      dp[l][r] = dp[l-1][r] + abs(l - i)*a
    else:
      dp[l][r] = max(dp[l-1][r]+abs(l-i)*a, dp[l][r-1]+abs(N-r+1-i)*a)

ans = 0
for l in range(N+1):
  r = N - l
  ans = max(ans, dp[l][r])

print(ans)