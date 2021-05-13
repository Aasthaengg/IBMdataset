def split(word): 
    return [char for char in word] 
MOD=10**9+7
h,w,k1=map(int,input().split())
dp=[]
for i in range(h+1):
  dp.append([])
  for j in range(w):
    dp[-1].append(0)
dp[0][0]=1
connections=[0]*(w-1)
totallegal=0
for i in range(pow(2,w-1)):
  s='{0:b}'.format(i)
  k=split(s)
  k.reverse()
  for j in range(w-1-len(k)):
    k.append('0')
  k.reverse()
  failflag=0
  for j in range(1,w-1):
    if k[j]=='1' and k[j-1]=='1':
      failflag=1
  if failflag==1:
    continue
  for j in range(w-1):
    if k[j]=='1':
      connections[j]+=1
  totallegal+=1
for i in range(h):
  for j in range(w):
    used=0
    if j>0:
      dp[i+1][j-1]=(dp[i+1][j-1]+connections[j-1]*dp[i][j])%MOD
      used+=connections[j-1]
    if j<w-1:
      dp[i+1][j+1]=(dp[i+1][j+1]+connections[j]*dp[i][j])%MOD
      used+=connections[j]
    dp[i+1][j]=(dp[i+1][j]+(totallegal-used)*dp[i][j])%MOD
print(dp[h][k1-1])