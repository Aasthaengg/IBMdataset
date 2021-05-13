n,k=map(int,input().split())
a=list(map(int,input().split()))
#n,k=100000,100
#a=[i for i in range(100000)]

kl=[i for i in range(1,k+1)]

dp=[float("inf")]*(n)
dp[0]=0
for i in range(1,n):
  dp[i] = min(dp[j] + abs(a[i] - a[j]) for j in range(max(0, i - k), i))

print(dp[n-1])
