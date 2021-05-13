ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k=nm()
h=nl()

dp = [10**10] * n
dp[0] = 0

for i in range(n):
  for j in range(i+1,min(i+k+1,n)):
    dp[j] = min(dp[j], dp[i] + abs(h[j]-h[i]))

print(dp[n-1])
