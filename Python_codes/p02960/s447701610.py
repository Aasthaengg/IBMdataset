MOD=10**9+7
S=input()

dp=[]
for i in range(len(S)+1):
  dp.append([0]*13)
dp[0][0]=1
#print(dp)

for i in range(1,len(S)+1):
  if S[i-1]=="?":
    for k in range(13):
      for j in range(10):
        dp[i][(10*k+j)%13]+=dp[i-1][k]
        dp[i][(10*k+j)%13]%=MOD
  else:
    si=int(S[i-1])
    for k in range(13):
      dp[i][(10*k+si)%13]+=dp[i-1][k]
      dp[i][(10*k+si)%13]%=MOD
    
#print(dp)
print(dp[-1][5])