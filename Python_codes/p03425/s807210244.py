n=int(input())
import collections
import itertools
l=['M','A','R','C','H']
x=[]
for i in range(n):
  s=input()
  if s[0] in l:
    x.append(s[0])
c=collections.Counter(x)
ans=0
for p in itertools.combinations('MARCH',3):
  cnt=1
  for j in range(3):
    cnt*=c[p[j]]
  ans+=cnt
print(ans)