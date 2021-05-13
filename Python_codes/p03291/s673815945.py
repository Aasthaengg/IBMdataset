MOD=10**9+7
dp=[[0]*5 for _ in range(210000)]

def add(a,b):
  ret_val=a+b
  if ret_val>=MOD:
    ret_val-=MOD
  return ret_val

S=input()

dp[0][0]=1
for i in range(len(S)):
  for j in range(5):
    if S[i]!="?":
      temp=add(dp[i+1][j],dp[i][j])
      dp[i+1][j]=temp
    else:
      temp=add(dp[i+1][j],dp[i][j]*3%MOD)
      dp[i+1][j]=temp

  if S[i]=="A" or S[i]=="?":
    temp=add(dp[i+1][1],dp[i][0])
    dp[i+1][1]=temp
  if S[i]=="B" or S[i]=="?":
    temp=add(dp[i+1][2],dp[i][1])
    dp[i+1][2]=temp
  if S[i]=="C" or S[i]=="?":
    temp=add(dp[i+1][3],dp[i][2])
    dp[i+1][3]=temp
print(dp[len(S)][3])
