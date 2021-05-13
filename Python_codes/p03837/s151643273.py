n,m = map(int,input().split())

import numpy as np
from scipy.sparse.csgraph import shortest_path

l = np.array([[float("inf") for i in range(n)] for j in range(n)])
from collections import defaultdict
ans = defaultdict(int)
for _ in range(m):
   a,b,c = map(int,input().split())
   l[a-1][b-1] = c
   l[b-1][a-1] = c
   if a > b:
      ans[(b,a)] = 1
   else:
      ans[(a,b)] = 1

d, p = shortest_path(l, return_predecessors=True)


for pp in p:
   for idx, ppp in enumerate(pp):
      if idx < ppp:
         ans[(idx+1,ppp+1)] = 0
      else:
         ans[(ppp+1,idx+1)] = 0
print(sum(ans.values()))