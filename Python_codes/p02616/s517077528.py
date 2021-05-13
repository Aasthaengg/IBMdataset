mod=10**9+7
n,k=map(int,input().split())
a=list(map(int,input().split()))
if max(a)<0:
  if k%2:a.sort(reverse=1)
  else:a.sort()
  ans=1
  for i in a[:k]:ans=(ans*i)%mod
  exit(print(ans))
if n==k:
  ans=1
  for i in a:ans=(ans*i)%mod
  exit(print(ans))
p=[(0,0)]
m=[(0,0)]
for i in a:
  if i<0:m.append((-i,1))
  else:p.append((i,0))
pp=mm=None
p.sort()
m.sort()
oe=0
ans=1
for i in range(k):
  if p[-1][0]>m[-1][0]:
    t,f=p.pop()
    pp=t
  else:
    t,f=m.pop()
    mm=t
  ans=(ans*t)%mod
  if ans==0:exit(print(0))
  oe^=f
if oe:
  if mm==None:
    ans=(ans*pow(pp,mod-2,mod)*m[-1][0])%mod
  elif pp==None:
    ans=(ans*pow(mm,mod-2,mod)*p[-1][0])%mod
  elif pp*p[-1][0]>mm*m[-1][0]:
    ans=(ans*pow(mm,mod-2,mod)*p[-1][0])%mod
  else:
    ans=(ans*pow(pp,mod-2,mod)*m[-1][0])%mod
print(ans)
