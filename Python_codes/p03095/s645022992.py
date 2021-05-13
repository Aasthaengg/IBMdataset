from collections import *
_=input()
c=Counter(input())
ans=1
for i in c.values():
    ans*=i+1
    ans%=10**9+7
print(ans-1)