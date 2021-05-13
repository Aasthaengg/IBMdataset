from collections import defaultdict
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[0]*(n+1)
d=defaultdict(int)
for i in range(1,n+1):
  b[i]=b[i-1]+a[i-1]
for i in range(n+1):
  d[b[i]%m]+=1
ans=0
for i in d.items():
  ans+=d[i[0]]*(d[i[0]]-1)//2
print(ans)