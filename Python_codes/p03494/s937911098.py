import numpy as np
n = int(input())
A = list(map(int, input().split()))
A = np.array(A)
cnt = 0
while all(a % 2 == 0 for a in A):
    A = A/2
    cnt += 1
print(cnt)

