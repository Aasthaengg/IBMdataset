from itertools import product
import numpy as np
from operator import itemgetter
N, M = map(int,input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

npa = np.array(a)

ans = -1000000000000
for pat in product([-1,1], repeat=3):
  #print(pat)
  npw = np.zeros(N)
  npw = np.dot(npa, np.array(pat).T)
  sort_reverse = np.sort(npw)[::-1]
  sums = sort_reverse[:M].sum()
  ans = max(ans, sums)
  
print(ans)