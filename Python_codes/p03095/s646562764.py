#解説参照済み
n=int(input())
a=list(input())
from collections import defaultdict
d=defaultdict(int)
for i in a:
    d[i]+=1
cnt=[]
for i in d.values():
    cnt.append(i+1)
ans=1
mod=10**9+7
for i in cnt:
    ans*=i
    ans%=mod
print(ans-1)