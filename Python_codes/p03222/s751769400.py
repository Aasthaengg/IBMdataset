import sys
h,w,k=map(int,input().split())
mod=10**9+7
if w==1:
  print(1)
  sys.exit()
b=[]
for i in range(2**(w-1)):
  b.append(format(i,'0'+str(w-1)+'b'))
l=[]
for i in range(len(b)):
  ct=0
  for j in range(w-2):
    if b[i][j]!='1' or b[i][j+1]!='1':
      ct+=1
  if ct==w-2:
    l.append(b[i])

count=[[0,0,0] for i in range(w)]
for i in range(len(l)):
  if l[i][0]=='0':
    count[0][1]+=1
  if l[i][0]=='1':
    count[0][2]+=1
  if l[i][-1]=='1':
    count[-1][0]+=1
  if l[i][-1]=='0':
    count[-1][1]+=1
  for j in range(w-2):
    if l[i][j:j+2]=='10':
      count[j+1][0]+=1
    if l[i][j:j+2]=='00':
      count[j+1][1]+=1
    if l[i][j:j+2]=='01':
      count[j+1][2]+=1

dp=[[0 for i in range(w)] for j in range(h+1)]
dp[0][0]=1
for i in range(h+1):
  for j in range(w):
    dp[i][j]+=dp[i-1][j]*count[j][1]
    dp[i][j]%=mod
    if j-1>=0:
      dp[i][j]+=dp[i-1][j-1]*count[j-1][2]
      dp[i][j]%=mod
    if j+1<=w-1:
      dp[i][j]+=dp[i-1][j+1]*count[j+1][0]
      dp[i][j]%=mod
print(dp[h][k-1]%mod)