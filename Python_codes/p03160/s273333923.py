N=int(input())
h=[int(x) for x in input().split()]
dp=[-1 for i in range(N)]
for i in range(N):
  if i==0:
    dp[N-1]=0
  elif i==1:
    dp[N-2]=abs(h[N-1]-h[N-2])
  else:
    dp[N-i-1]=min(dp[N-i]+abs(h[N-i]-h[N-i-1]),dp[N-i+1]+abs(h[N-i+1]-h[N-i-1]))
print(dp[0])