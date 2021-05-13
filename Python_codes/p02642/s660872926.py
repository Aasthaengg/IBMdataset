import numpy as np
from collections import Counter
n = int(input())
aa = list(map(int, input().split()))
ngs = np.zeros((10**6)+1, dtype=int)

for a in set(aa):
    ngs[2*a::a] = 1
    
dic = Counter(aa)
times = np.array(list(dic.keys()))[np.array(list(dic.values())) > 1]

for i in times:
    ngs[i] = 1
cnt = 0
for a in aa:
    cnt += 1-ngs[a]
print((cnt))