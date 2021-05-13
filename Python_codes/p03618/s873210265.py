a=list(input())
ans=len(a)*(len(a)-1)//2
import collections
J=dict(collections.Counter(a))
for i in J.values():
    ans-=i*(i-1)//2
print(ans+1)