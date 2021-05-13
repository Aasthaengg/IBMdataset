n=int(input())
a=[int(j) for j in input().split()]
mod=10**9+7
ans=1
from collections import Counter
c=Counter()
c[0]+=3
for i in a:
    ans*=c[i]
    if ans==0:
        break
    c[i]-=1
    c[i+1]+=1
    ans%=mod
print(ans)