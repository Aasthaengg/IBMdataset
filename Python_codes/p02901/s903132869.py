N,M=map(int,input().split())

def conv_to_bit(clist):
  ret=0
  for c in clist:
    ret+=2**(c-1)
  return ret

alist=[]
cmat=[]
for i in range(M):
  a,b=map(int,input().split())
  alist.append(a)
  clist=list(map(int,input().split()))
  cmat.append(clist)
  
dp=[]
for i in range(M+1):
  dp.append([float("inf")]*(2**N))
dp[0][0]=0
  
for i in range(M):
  cbit=conv_to_bit(cmat[i])
  for j in range(2**N):
    dp[i+1][j]=dp[i][j]

  for j in range(2**N):
    bit_or=j|cbit
    dp[i+1][bit_or]=min(dp[i+1][bit_or],dp[i][j]+alist[i])
    
if dp[-1][-1]==float("inf"):
  print(-1)
else:
  print(dp[-1][-1])