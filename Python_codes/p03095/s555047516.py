from collections import Counter
mod=10**9+7 
input()
s=list(input())
c=Counter(s)
ans=1
for i in c.values():
    ans*=(i+1)
    ans%=mod
ans-=1
ans%=mod
print(ans)