a=int(input())
l=list(map(int, input().split()))
import collections
c = collections.Counter(l)
ans=0
for k in c:
  if k>c[k]:
    ans+=c[k]
  else:
    ans+=c[k]-k
print(ans)