n,m=map(int,input().split())
ab=[]
c=[]
for _ in range(m):
  ab.append(list(map(int,input().split())))
  c.append(list(map(int,input().split())))
dp={'0'*n:0}
for i in range(m):
  a,b=ab[i]
  ci=c[i]
  dptmp={}
  for k,v in dp.items():
    s=list(k)
    for cii in ci:
      s[cii-1]='1'
    t=''.join(s)
    dptmp[t]=min(v+a,dp[t] if t in dp else float('inf'),dptmp[t] if t in dptmp else float('inf'))
  dp.update(dptmp)

t='1'*n
if t in dp:
  print(dp[t])
else:
  print(-1)
#print(dp)