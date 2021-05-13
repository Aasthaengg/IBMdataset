import collections
S=list(input())
a=len(S)
ans=(a*(a-1))//2
ans+=1
c = collections.Counter(S)
for b in c.values():
  ans-=(b*(b-1))//2
print(ans)