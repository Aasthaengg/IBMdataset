K, S = map(int, input().split())
cnt = 0
from itertools import product as prd
for x, y in prd(range(K+1),range(K+1)):
    if 0 <= S-x-y <= K:
        cnt += 1
print(cnt)