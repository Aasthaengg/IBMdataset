n,c=map(int,input().split())
L=R=Rmax=0
x=[0]*n
v=[0]*n
for i in range(n):
  xx,vv=map(int,input().split())
  x[i]=xx
  v[i]=vv
  L+=vv
ans=L-x[-1]
for i in reversed(range(n)):
  L-=v[i]
  R+=v[i]
  Rmax=max(Rmax,R-(c-x[i]))
  ans=max(ans,L-(x[i-1]*2 if i>0 else 0)+Rmax)
Lmax=0
for i in range(n):
  L+=v[i]
  R-=v[i]
  Lmax=max(Lmax,L-x[i])
  ans=max(ans,R-((c-x[i+1])*2 if i<n-1 else 0)+Lmax)
print(ans)