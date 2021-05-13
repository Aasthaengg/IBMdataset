n,k = map(int,input().split())
l = list(map(int,input().split()))
dp = [float("inf")]*(n+1)
for i in range(n):
  if i ==0:
    dp[0]=0
  for j in range(1,k+1):
    if i-j>=0:
    	dp[i]=min(dp[i],dp[i-j]+abs(l[i]-l[i-j]))
print(dp[n-1])
