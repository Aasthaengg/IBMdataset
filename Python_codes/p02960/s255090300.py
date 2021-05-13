MOD=10**9+7

S=input()
old=[0]*13
old[0]=1
n=1
for c in S:
  dp=[0]*13
  if c=='?':
    for j in range(10):
      for i in range(13):
        dp[(i*10+j)%13]+=old[i]
        dp[(i*10+j)%13]%=MOD
  else:
    c=int(c)
    for i in range(13):
      dp[(i*10+c)%13]+=old[i]
      dp[(i*10+c)%13]%=MOD
  old=[i for i in dp]
print(dp[5])