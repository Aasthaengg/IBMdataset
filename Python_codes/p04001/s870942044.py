A = list(map(int, list(input())))
 
ans = 0
from itertools import *
N = len(A)-1
for p in product([0,1],repeat=N):
    now = A[0]
    for i in range(N):
        if p[i] == 0:
            now = now*10+A[i+1]
        else:
            ans += now
            now = A[i+1]
    ans += now
print(ans)