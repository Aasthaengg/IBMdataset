from itertools import permutations
from collections import Counter

N,*xyf = map(int, open(0).read().split())
xy = [(xyf[i*2],xyf[i*2+1]) for i in range(N)]
if N == 1:
    print(1)
else:
    count = []
    for a, b in permutations(xy,2):
        count.append((b[0]-a[0],b[1]-a[1]))
    c = Counter(count)
    print(N-max(c.values()))