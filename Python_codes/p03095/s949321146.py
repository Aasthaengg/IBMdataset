from collections import Counter
mod=10**9+7
n=int(input())
s=input()
c=Counter(s).values()
ans=1
for i in c:
    ans*=(i+1)
    ans%=mod
    
print(ans-1)