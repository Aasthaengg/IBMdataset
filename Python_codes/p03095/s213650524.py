n=int(input())
s=list(input())
mod=10**9+7
from collections import Counter
c=Counter(s)
ans=1
for k in c.keys():
    ans*=(c[k]+1)%mod
    ans%=mod
print((ans+mod-1)%mod)