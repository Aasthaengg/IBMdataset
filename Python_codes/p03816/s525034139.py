n,*l=map(int,open(0).read().split())
from collections import *
c=Counter(l)
print(len(c)-sum(1-v%2 for v in c.values())%2)