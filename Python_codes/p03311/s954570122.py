import numpy as np
from statistics import median

N = int(input())
A = list(map(int, input().split()))
list_n = list(range(1, (N+1), 1))
A_tmp = np.array(A)
list_n_tmp = np.array(list_n)
list_diff = A_tmp - list_n_tmp
b = median(list_diff)
Xtmp = 0

for n in range(0, N, 1):
    Xtmp += abs(A[n] - (b + n + 1))

print(int(Xtmp))
