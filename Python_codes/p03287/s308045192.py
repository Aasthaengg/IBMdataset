n,m=map(int,input().split())
a=list(map(int,input().split()))

wa=[0]
temp=0
for i in a:
  temp+=i
  wa.append(temp%m)

from collections import Counter
c=Counter(wa) #各余りが何種類あるか分析したよ。

ans=0
from operator import mul
from functools import reduce

def cmb(n,r):
    if n<r: return 0
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

for i in c.values():
  ans+=cmb(i,2)
print(ans)