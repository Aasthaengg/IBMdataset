n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
f=sorted(list(map(int,input().split())),reverse=True)
d=[[a[i]*f[i],f[i]] for i in range(n)]
r=max([di[0] for di in d])+1
l=0
x=(l+r)//2
while r-l>1:
  if r-l==2:
    cnt=0
    for di,fi in d:
      cnt+=max(0,(di-l+fi-1)//fi)
    if cnt<=k:
      x=l
    else:
      x=l+1
    break
  cnt=0
  for di,fi in d:
    cnt+=max(0,(di-x+fi-1)//fi)
  if cnt>k:
    l,r=x,r
  else:
    l,r=l,x+1
  x=(l+r)//2
if r-l==2:
  if cnt>k:
    x=l+1
  else:
    x=l

print(x)
