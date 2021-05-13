n=int(input())
s=input()
l=[s[i] for i in range(n)]
import collections
c=collections.Counter(l)
mod=10**9+7
li=list(c.values())
ans=1
for i in li:
  ans*=1+i
  ans%=mod
print(ans-1)