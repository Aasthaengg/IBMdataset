import itertools
import collections
l=[list(map(int,input().split())) for _ in range(3)]
l=list(itertools.chain(*l))
c=collections.Counter(l)
if sorted(list(c.values()))==[1,1,2,2]:
    print("YES")
else:
    print("NO")
