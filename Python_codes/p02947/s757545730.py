S=[]
n = int(input())
for i in range(n):
    s=''.join(sorted(input()))
    S.append(s)
import collections
from scipy.special import comb
a=0
Sd=list(set(S))
c = collections.Counter(S)
for p in  range(len(Sd)):
    if c[Sd[p]] >=2:
        a  += comb(c[Sd[p]], 2, exact=True)
print(a)