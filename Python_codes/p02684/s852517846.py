n,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
c=[0]*(n+1)
c[1]=1
q=[0,1]
while True:
  i=a[q[-1]]
  if c[i]:break
  c[i]=c[q[-1]]+1
  q+=[i]
if c[i]<k:
  k-=c[i]-1
  t=c[q[-1]]-c[i]+1
  print(q[c[i]+k%t])
else:print(q[k+1])