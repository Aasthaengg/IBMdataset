L=input()
DIV=10**9+7
dp=[[0 for i in range(2)] for j in range(len(L))]

dp[0][0]=2
dp[0][1]=1

for i in range(1,len(L)):
  x=int(L[i])
  dp[i][0]=(dp[i-1][0]*2*(x==1)+dp[i-1][0]*1*(x==0))%DIV
  dp[i][1]=(dp[i-1][0]*1*(x==1)+dp[i-1][1]*3)%DIV

print((dp[-1][0]+dp[-1][1])%DIV)
