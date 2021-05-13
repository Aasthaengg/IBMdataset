N=int(input())
S=list(input())

from collections import*
C=Counter(S)

ans=1
for c in C.values():
    ans*=(c+1)%(10**9+7)
ans=(ans-1)%(10**9+7)

print(ans)