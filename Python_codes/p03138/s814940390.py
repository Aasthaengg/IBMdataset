N,K=map(int,input().split())
A=list(map(int,input().split()))

keta=len(bin(max(K,max(A)))[2:])

cnt1=[0]*keta
cnt0=[0]*keta

for i in range(len(A)):
  for j in range(keta):
    if (A[i]>>j)&1:
      cnt1[keta-1-j]+=1
    else:
      cnt0[keta-1-j]+=1

Ks=bin(K)[2:].zfill(keta)
dp=[[[0 for i in range(2)] for j in range(2)] for k in range(len(Ks))]
def calc(di,v):
  unit=2**(keta-1-di)
  if v==0:
    return cnt1[di]*unit
  else:
    return cnt0[di]*unit

x0=int(Ks[0])
dp[0][0][0]=(0 if x0==1 else calc(0,0))
dp[0][0][1]=(0 if x0==0 else calc(0,1))
dp[0][1][0]=(0 if x0==0 else calc(0,0))
dp[0][1][1]=0

for i in range(1,len(dp)):
  x=int(Ks[i])
  if x==0:
    dp[i][0][0]=dp[i-1][0][0]+dp[i-1][0][1]+calc(i,0)
    dp[i][0][1]=0
  else:
    dp[i][0][0]=0
    dp[i][0][1]=dp[i-1][0][0]+dp[i-1][0][1]+calc(i,1)
  dp[i][1][0]=max(dp[i-1][0][0]*(x==1),dp[i-1][0][1]*(x==1),dp[i-1][1][0],dp[i-1][1][1])+calc(i,0)
  dp[i][1][1]=max(dp[i-1][1][0],dp[i-1][1][1])+calc(i,1)

ans=0
for i in range(2):
  for j in range(2):
    if ans<dp[len(dp)-1][i][j]:
      ans=dp[len(dp)-1][i][j]
print(ans)
