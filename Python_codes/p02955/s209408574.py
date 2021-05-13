n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a)
ii=[]
for i in range(1,int(s**0.5)+1):
  if s%i>0:
    continue
  ii+=[i,s//i]
ii.sort(reverse=True)
for i in ii:
  r=[]
  for j in range(n):
    r+=[a[j]%i]
  r.sort()
  b=0
  l=0
  while l<n and b+r[l]<=k:
    b+=r[l]
    l+=1
  if sum([i-x for x in r[l:]]) <= k:
    print(i)
    break