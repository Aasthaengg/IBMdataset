n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
from collections import defaultdict
mods=defaultdict(int)
mods[0]=1
for i in range(1,len(a)):
  a[i]=a[i-1]+a[i]%m
  mods[a[i]%m]+=1
ans=0
for v in mods.values():
  if v>1:
    ans+=v*(v-1)//2
print(ans)