from itertools import accumulate
import bisect
n = int(input())
A = [n for n in range(1,5*10**3)]
B = list(accumulate(A))
i = bisect.bisect_right(B, n)
if B[i-1] == n:
    for j in range(i):
        print(A[j])
else:
    k = B[i] - n
    for j in range(i+1):
        if A[j] == k:
            continue
        print(A[j])