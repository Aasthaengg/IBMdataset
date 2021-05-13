import numpy as np
n = int(input())
A = np.array([list(map(int,input().split())) for _ in range(n)])
s = np.argsort(A[:,1])
# B基準でソート
A = A[s]
a = 0
ans = 'Yes'
for i in range(n):
    a += A[i,0]
    b = A[i,1]
    if a > b:
        ans = 'No'
        break
print(ans)