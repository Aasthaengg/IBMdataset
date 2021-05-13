import numpy as np
n = int(input())
A = np.array([list(map(int,input().split())) for _ in range(n)])
s = np.argsort(A[:,1])
A = A[s]
aa = 0
ans = 'Yes'
for a,b in A:
    aa += a
    if aa > b:
        ans = 'No'
        break
print(ans)