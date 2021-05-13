n=int(input())
a,b,c=[],[],[]
for _ in range(n):
  A,B,C=map(int,input().split())
  a.append(A)
  b.append(B)
  c.append(C)
#print(a,b,c)
dp=[[[0] for _ in range(3)] for _ in range(n)]
dp[0][0]=a[0]
dp[0][1]=b[0]
dp[0][2]=c[0]
#print(dp)
for i in range(1,n):
  dp[i][0]=max(dp[i-1][1]+a[i],dp[i-1][2]+a[i])
  #print("dp[i][0]",dp[i][0],"dp[i-1][1]",dp[i-1][1],"dp[i-1][2]",dp[i-1][2],"a[i]",a[i])
  dp[i][1]=max(dp[i-1][0]+b[i],dp[i-1][2]+b[i])
  #print("dp[i][1]",dp[i][1],"dp[i-1][0]",dp[i-1][0],"dp[i-1][2]",dp[i-1][2],"b[i]",b[i])
  dp[i][2]=max(dp[i-1][0]+c[i],dp[i-1][1]+c[i])
  #print("dp[i][2]",dp[i][2],"dp[i-1][0]",dp[i-1][0],"dp[i-1][1]",dp[i-1][1],"c[i]",c[i])
  #print(i,dp)
#print(dp)
print(max(dp[-1][0],dp[-1][1],dp[-1][2]))

