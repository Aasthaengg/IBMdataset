n,m=[int(x) for x in input().split()]
s=[]
for i in range(m):
  k=[int(x) for x in input().split()]
  s.append(k)
p=[int(x) for x in input().split()]

import itertools
l=[]
a=itertools.product(range(2),repeat=n)
for i in a:
  l.append(i)

ans=0
for i in range(2**n):
  ok=[]
  for j in range(m):
    on=0
    for t in range(1,s[j][0]+1):
      e=s[j][t]
      if l[i][e-1]==1:
        on+=1
    if on%2!=p[j]:
      ok.append(False)
  if False not in ok:
    ans+=1

print(ans)