import sys
read=sys.stdin.read
readline=sys.stdin.readline

a,b,c,d,e,f=map(int,readline().split())

def searints(m,n,l):#m<=n
  mask=(1<<l+1)-1
  s=sum([1<<n*i for i in range(1,l//n+1)])&mask
  for i in range(1,l//m+1):
    s=(s+1<<m*i|s) &mask
  return [x for x in range(0,l+1) if ((s+1)>>x)&1==1]

w=searints(100*a,100*b,f)
s=searints(c,d,f)
candidates=[(100*y/(x+y),x+y,y) for x in w for y in s if e*x>=100*y and x*y>0 and x+y<=f]
if candidates:
  print(*max(candidates)[1:])
else:
  print(100*a,0)