ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
a = nl()

dp=[0]*(n+1)
dp[0] = 1000

for i in range(1,n):
  dp[i]=dp[i-1]
  for j in range(i):
    v = dp[j] // a[j]
    w = dp[j] + (a[i]-a[j])*v
    dp[i] = max(dp[i],w)
print(dp[n-1])
