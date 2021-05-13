from collections import defaultdict
n,t=map(int,input().split())
a=list(map(int,input().split()))
min_v=a[0]
div=0
for i in range(1,n):
  min_v=min(min_v,a[i])
  div=max(div,a[i]-min_v)
d=defaultdict(int)
for i in range(n):
  d[a[i]]=i
ans=0
for i in range(n):
  if d[a[i]]<d[a[i]+div]:
    ans+=1
print(ans)