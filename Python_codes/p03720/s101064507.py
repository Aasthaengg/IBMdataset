n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)] 

import itertools

abb = list(itertools.chain.from_iterable(ab))

from collections import Counter
count = Counter(abb)
for i in range(1,n+1):
    print(count[i])