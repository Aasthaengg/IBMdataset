n=int(input())
h=list(map(int,input().split()))
dp=[0]*(n)
for i in range(1,n):
  if i-2>=0:
    dp[i]=min(dp[i-1]+abs(h[i-1]-h[i]),dp[i-2]+abs(h[i-2]-h[i]))
  else:
    dp[i]=dp[i-1]+abs(h[i-1]-h[i])
print(dp[-1])