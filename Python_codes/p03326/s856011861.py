N,M=map(int,input().split())
cakes=[None]*N
for i in range(N):
  x,y,z=map(int,input().split())
  cakes[i]=[x,y,z]
  
ans=0
for i in range(2**3):
  plus_or_minus=[1]*3
  for j in range(3):
    if (i>>j)&1:
      plus_or_minus[j]=1
    else:
      plus_or_minus[j]=-1
  dp=[None for j in range(M+1)]
  dp[0]=[0,0,0]
  
  for c in range(len(cakes)):
    for j in range(c+1,-1,-1):
      if j<len(dp)-1 and dp[j]!=None:
        if dp[j+1]==None:
          dp[j+1]=[None]*3
          for k in range(3):
            dp[j+1][k]=dp[j][k]+cakes[c][k]
        else:
          diff=0
          for k in range(3):
            diff+=((dp[j][k]+cakes[c][k])*plus_or_minus[k])-(dp[j+1][k]*plus_or_minus[k])
          if diff>0:
            for k in range(3):
              dp[j+1][k]=dp[j][k]+cakes[c][k]
  if abs(dp[-1][0])+abs(dp[-1][1])+abs(dp[-1][2])>ans:
    ans=abs(dp[-1][0])+abs(dp[-1][1])+abs(dp[-1][2])

print(ans)
