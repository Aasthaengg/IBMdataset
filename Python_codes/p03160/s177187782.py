ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
h=nl()

dp=[10**5]*(n+1)

dp[0]=0

dp[1]=abs(h[1]-h[0])

for i in range(2,n):
  dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))


print(dp[n-1])
