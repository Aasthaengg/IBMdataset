import numpy as np
N = int(input())
A = [int(a) for a in input().split()]
ans = np.argsort(A) + 1

for a in ans:
    print(a, end=' ')
print()
