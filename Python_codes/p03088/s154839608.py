N=int(input())
MOD=10**9+7
dp=[[0]*4 for i in range(N)]
for i in range(4):
  dp[0][i]=1
  dp[1][i]=4
dic={'AG':1,'AC':1,'GA':1,'AGA':0,'AGG':0,'AGT':0,'AAG':0,'ATG':0,'AA':1,'AT':1}
def chk(i,j):
  global dp,dic
  if j==0:
    return 0
  elif j==1:
    return dic['AGG']+dic['AGT']+dic['ATG']+dic['AG']+dic['GA']
  elif j==2:
    return dic['AC']
  else:
    return 0
dp[2][0]=sum(dp[1])
dp[2][1]=sum(dp[1])-dp[0][0]-dp[0][2]
dp[2][2]=sum(dp[1])-dp[0][0]
dp[2][3]=sum(dp[1])
#dic['AGA']=dic['AG']
dic['AGG']=dic['AG']
dic['AGT']=dic['AG']
#dic['AAG']=dic['AA']
dic['ATG']=dic['AT']
dic['AG']=dp[1][0]
dic['AC']=dp[1][0]-dic['GA']
dic['GA']=dp[1][2]
dic['AT']=dp[1][0]
for i in range(3,N):
  _=sum(dp[i-1])
  for j in range(4):
    dp[i][j]=_-chk(i,j)
  dic['AGG']=dic['AG']
  dic['AGT']=dic['AG']
  dic['ATG']=dic['AT']
  dic['AG']=dp[i-1][0]
  dic['AC']=dp[i-1][0]-dic['GA']
  dic['GA']=dp[i-1][2]
  dic['AT']=dp[i-1][0]
print(sum(dp[-1])%MOD)