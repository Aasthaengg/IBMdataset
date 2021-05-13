H,W=map(int,input().split())
dp=[[0 for i in range(W)] for k in range(H)]
ALL=[]
for i in range(H):
  S=input()
  ALL+=[S]
  for k in range(W):
    if i==0 and k==0:
      if S[k]=="#":
        dp[i][k]=1
      else:
        dp[i][k]=0
    elif i==0:
      if S[k]=="#" and S[k-1]=="#":
        dp[i][k]=dp[i][k-1]
      elif S[k]=="." and S[k-1]==".":
        dp[i][k]=dp[i][k-1]
      elif S[k]=="." and S[k-1]=="#":
        dp[i][k]=dp[i][k-1]
      else:
        dp[i][k]=dp[i][k-1]+1
    elif k==0:
      if S[k]=="#" and ALL[i-1][k]=="#":
        dp[i][k]=dp[i-1][k]
      elif S[k]=="." and ALL[i-1][k]==".":
        dp[i][k]=dp[i-1][k]
      elif S[k]=="." and ALL[i-1][k]=="#":  
        dp[i][k]=dp[i-1][k]
      else:
        dp[i][k]=dp[i-1][k]+1
    else:
      if S[k]=="#":
        if S[k-1]=="#" and ALL[i-1][k]=="#":
          dp[i][k]=min(dp[i][k-1],dp[i-1][k])
        elif S[k-1]=="#" and ALL[i-1][k]==".":
          dp[i][k]=min(dp[i][k-1],dp[i-1][k]+1)
        elif S[k-1]=="." and ALL[i-1][k]=="#":
          dp[i][k]=min(dp[i][k-1]+1,dp[i-1][k])
        else:
          dp[i][k]=min(dp[i][k-1],dp[i-1][k])+1
      else:
        dp[i][k]=min(dp[i][k-1],dp[i-1][k])        
ans=dp[H-1][W-1]
print(ans)