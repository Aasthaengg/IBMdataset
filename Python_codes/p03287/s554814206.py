import numpy as np
from collections import Counter

N,M = map(int, input().split())
An = [0] + list(map(int, input().split()))
An = np.array(An)

_ = Counter(np.cumsum(An%M) % M)
ans = 0
for i in _.values():
  ans += i*(i-1)//2

print(ans)