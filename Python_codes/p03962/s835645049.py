l= list(map(int,input().split()))

import collections

c=collections.Counter(l)
print(len(c.keys()))