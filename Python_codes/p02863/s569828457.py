n,t=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
arr=sorted(arr,key=lambda x:x[1])
arr=sorted(arr,key=lambda x:x[0])
dp=[[0]*3001 for _ in range(n+1)]
maxs=[0]
for i in range(n-2,-1,-1):
  maxs.append(max(maxs[-1],arr[i+1][1]))
maxs=maxs[::-1]
for i in range(n):
  a,b=arr[i]
  for j in range(t):
    if j-a<0:
      continue
    dp[i+1][j]=max(dp[i][j],dp[i][j-a]+b)
  dp[i+1][a]=max(dp[i][a],b)
ans=0
for i in range(n):
  tmp=max(dp[i+1][:t])+maxs[i]
  ans=max(ans,tmp)
print(ans)