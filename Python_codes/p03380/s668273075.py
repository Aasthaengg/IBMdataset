# D - Binomial Coefficients

import sys
readline = sys.stdin.readline

n = int(readline())
A = list(int(a) for a in readline().split())
A.sort(reverse=True)

N = A[0]
R = 0
tmpR = 0
for i in range(1, n):
    tmp = min(A[i], N-A[i])
    if tmpR < tmp:
        tmpR = tmp
        R = A[i]       

print(N, R)