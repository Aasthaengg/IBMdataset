l=input()
n=len(l)
import collections
c=collections.Counter(l)
ans=n*(n-1)//2+1
for i,j in c.items():
    ans-=j*(j-1)//2
print(ans)