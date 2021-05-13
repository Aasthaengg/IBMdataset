n,k=map(int,input().split())
a=list(map(int,input().split()))
d={}
ans=0
for i in range(n):
  if a[i] in d: d[a[i]]+=1
  else: d[a[i]]=1
dd = sorted(d.values(), reverse = True)
if len(dd)<=k:
  print(0)
else:
  ans=n
  for i in range(k):
    ans -= dd[i]
  print(ans)