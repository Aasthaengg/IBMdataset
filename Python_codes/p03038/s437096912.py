from collections import defaultdict
n,m=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort()
bc=defaultdict(int)
for i in range(m):
  b,c=map(int,input().split())
  bc[c]+=b
i=0
newc=[0]*n
for c,b in sorted(bc.items(),key=lambda x:x[0],reverse=True):
  for _ in range(b):
    if i==n:
      break
    newc[i]=c
    i+=1
ans=sum(a)
for i in range(n):
  if newc[i]>a[i]:
    ans+=newc[i]-a[i]
print(ans)