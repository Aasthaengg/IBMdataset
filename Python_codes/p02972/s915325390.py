n=int(input())
a=[0]+list(map(int,input().split()))
b=[0]*(n+1)
for i in range(n,0,-1):
  s=0
  t=i
  while t<=n:
    s+=b[t]
    t+=i
  if s%2==a[i]:
    pass
  else:
    b[i]=1
ans=0
c=[]
for i,bb in enumerate(b):
  if bb>0:
    ans+=bb
    c.append(i)
if ans>0:
  print(ans)
  print(*c)
else:
  print(0)