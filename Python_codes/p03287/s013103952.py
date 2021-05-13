import numpy as np
from collections import Counter
n,m = map(int,input().split())
A = np.cumsum([0]+list(map(int,input().split())),dtype="int64")%m

C = Counter(A)
ans = 0
for c in C.values():
	c -= 1
	ans += c*(c+1)//2
print(ans)