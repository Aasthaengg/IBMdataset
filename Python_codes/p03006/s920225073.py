(n,),*xy = [list(map(int, s.split())) for s in open(0)]

from collections import Counter
from itertools import combinations
from sys import exit

if n == 1:
    print(1)
    exit()

c = Counter()

for (xa,ya),(xb,yb) in combinations(xy,2):
    c[(xa-xb, ya-yb)] += 1
    c[(xb-xa, yb-ya)] += 1

print(n - max(c.values()))