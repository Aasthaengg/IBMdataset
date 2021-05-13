N,A,B=map(int,input().split())
xlist=list(map(int,input().split()))

dp=[float("inf")]*N
dp[0]=0

for i in range(1,N):
  dp[i]=min(dp[i-1]+A*(xlist[i]-xlist[i-1]),dp[i-1]+B)
  
print(dp[N-1])