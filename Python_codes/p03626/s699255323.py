MOD=10**9+7
N=int(input())

mat=[]
for i in range(2):
  mat.append(list(input()))
#print(mat)

dp=[1]+[0]*N
i=1
while i<N+1:
  if mat[0][i-1]==mat[1][i-1]:
    if i==1:
      dp[1]=3
    else:
      if mat[0][i-2]==mat[1][i-2]:
        dp[i]=2*dp[i-1]
        dp[i]%=MOD
      else:
        dp[i]=dp[i-1]
  else:
    if i==1:
      dp[1]=dp[2]=6
      i+=1
    else:
      if mat[0][i-2]==mat[1][i-2]:
        dp[i]=dp[i+1]=2*dp[i-1]
        dp[i]%=MOD
        dp[i+1]%=MOD
        i+=1
      else:
        dp[i]=dp[i+1]=3*dp[i-1]
        dp[i]%=MOD
        dp[i+1]%=MOD
        i+=1
  i+=1
        
#print(dp)
print(dp[-1])