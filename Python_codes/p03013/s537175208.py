n,m=map(int,input().split())
p = 10**9+7
a=[1] * (n+1)
for i in range(m):
  a[int(input())] =0

dp = [0] * (n+1)
dp[0]=1
dp[1]=1 if a[1] else 0
for i in range(2,n+1):
  dp[i] = a[i] * (dp[i-2]*a[i-2] + dp[i-1]*a[i-1]) % p
print(dp[n]%p)