from itertools import*
n,k=map(int,input().split())
v=list(map(int,input().split()))
ans=0
for i in range(k+1):
  if i>n:break
  for j in range(i+1):
    c=0
    d=sorted(v[:j]+v[n-i+j:])
    l=k-len(d)
    for m in d:
      if m<0 and l:
        l-=1
        continue
      c+=m
    ans=max(ans,c)
print(ans)