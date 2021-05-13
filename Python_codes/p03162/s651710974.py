n=int(input())

dp=[[0 for _ in range(3)] for _ in range(n+1)]

for i in range(3):
  dp[0][i]=0
  
a=[]


  
for _ in range(n):
  d=list(map(int,input().split()))
  a.append(d)
  
for x in range(n):
  for y in range(3):
    for z in range(3):
      if y!=z:
        dp[x+1][z]=max(dp[x+1][z],dp[x][y]+a[x][z])
        
print(max(dp[n][0],dp[n][1],dp[n][2]))