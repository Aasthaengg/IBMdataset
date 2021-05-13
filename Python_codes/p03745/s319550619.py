# A - Sorted Arrays
import numpy as np

N = int(input())
A = list(map(int, input().split()))
sgn = 0
ans = 1

for i in range(N-1):
    tmp = np.sign(A[i+1]-A[i])
    if tmp*sgn<0:
        ans += 1
        sgn = 0
    else:
        sgn = np.sign(2*sgn+tmp)

print(ans)