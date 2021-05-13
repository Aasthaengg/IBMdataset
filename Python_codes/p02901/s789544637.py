from operator import itemgetter
n,m=map(int,input().split())
l=[]
for i in range(m):
  l2=[]
  a,b=map(int,input().split())
  l2.append(a)
  x=list(map(int,input().split()))
  ct=0
  for i in range(n):
    if i+1 in x:
      ct+=2**i
  l2.append(ct)
  l.append(l2)

dp=[[999999999999 for i in range(2**n)] for j in range(m+1)]
dp[0][0]=0
for i in range(1,m+1):
  for j in range(2**n):
    dp[i][j|l[i-1][1]]=min(dp[i-1][j]+l[i-1][0],dp[i][j|l[i-1][1]])
  for j in range(2**n):
    dp[i][j]=min(dp[i][j],dp[i-1][j])

if dp[m][2**n-1]<10**11:
  print(dp[m][2**n-1])
else:
  print(-1)
