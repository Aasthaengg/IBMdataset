n,m=map(int,input().split())
from collections import Counter as co

from itertools import chain
flatten=chain.from_iterable
print("YES" if all(i%2==0 for i in co(flatten([list(map(int,input().split())) for i in range(m)])).values()) else "NO")