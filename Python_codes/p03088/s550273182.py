MOD=10**9+7
N=int(input())
if N==3:
  print(61)
  exit()
  
dp=[[[[1]*4 for c in range(4)] for b in range(4)] for a in range(4)]
        
for x in range(4):
  dp[0][x][2][1]=0
  dp[0][2][x][1]=0
  dp[0][1][2][x]=0
  dp[2][0][1][x]=0
  dp[0][2][1][x]=0
  dp[x][0][1][2]=0
  dp[x][2][0][1]=0
  dp[x][0][2][1]=0
  
def f():
  tmp=[[[[0]*4 for c in range(4)] for b in range(4)] for a in range(4)]
  for a in range(4):
    for b in range(4):
      for c in range(4):
        t=sum([dp[x][a][b][c] for x in range(4)])
        t%=MOD
        for d in range(4):
          tmp[a][b][c][d]=t
          
  for x in range(4):
    tmp[0][x][2][1]=0
    tmp[0][2][x][1]=0
    tmp[x][0][1][2]=0
    tmp[x][2][0][1]=0
    tmp[x][0][2][1]=0
    
  return tmp
  
for k in range(4, N):
  dp=f()
  
print(sum([sum([dp[a][b][c][d] for a in range(4) for b in range(4) for c in range(4)])%MOD for d in range(4)])%MOD)