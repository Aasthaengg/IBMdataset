n=int(input())
A,G,C,T,mod,ans=0,1,2,3,pow(10,9)+7,0
dp=[[[[0]*4for k in range(4)]for j in range(4)]for i in range(n+1)]
dp[0][T][T][T]=1
for i in range(1,n+1):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        for m in range(4):
          if(G,A,C)!=(k,l,m)!=(A,C,G)!=(k,l,m)!=(A,G,C)!=(j,l,m)!=(A,G,C)!=(j,k,m):
            dp[i][k][l][m]+=dp[i-1][j][k][l]
            dp[i][k][l][m]%=mod
for j in range(4):
  for k in range(4):
    for l in range(4):
      ans+=dp[n][j][k][l]
print(ans%mod)