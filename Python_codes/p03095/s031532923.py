A=int(input())
l=list(input())
mod=10**9+7
import collections
l=list(collections.Counter(l).values())
l=[i+1 for i in l]
ans=1
for i in l:
   ans*=i
   ans%=mod
print(ans-1)