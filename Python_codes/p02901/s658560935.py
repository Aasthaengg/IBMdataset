n,m=map(int,input().split())
dp=[]
INF=10**9
for i in range(m+1):
  dp.append([])
  dp[-1].append(0)
  for j in range(2**n-1):
    dp[-1].append(INF)
keys=[]
for i in range(m):
  a,b=map(int,input().split())
  r=['0']*n
  c=list(map(int,input().split()))
  for j in range(b):
    r[c[j]-1]='1'
  s=''.join(r)
  keys.append([int(s,2),a])
    
for i in range(m):
  for j in range(2**n):
    dp[i+1][j|keys[i][0]]=min(dp[i+1][j|keys[i][0]],dp[i][j]+keys[i][1])
    dp[i+1][j]=min(dp[i+1][j],dp[i][j])
if dp[m][2**n-1]==10**9:
  print(-1)
else:
  print(dp[m][2**n-1])