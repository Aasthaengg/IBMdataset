from itertools import accumulate
from collections import defaultdict
N,K = map(int, input().split())
Xs = list(accumulate([0] + [int(x) for x in input().split()]))
Xs = [(x-i)%K for i, x in enumerate(Xs)]
d,r=defaultdict(int),0
for i, x in enumerate(Xs):
    d[x]+=1
    if i >= K:
        d[Xs[i-K]] -= 1
    r += d[x]-1
print(r)
