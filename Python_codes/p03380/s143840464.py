import sys
import bisect
n = int(input())
A = list(map(int,input().split()))
A.sort()
m = A[-1]
if n == 2:
    print(A[-1],A[0])
    sys.exit()
i = bisect.bisect_left(A,m//2)
if i == 0:
    print(m,A[0])
else:
    if m - A[i] < A[i-1]:
        print(m,A[i-1])
    else:
        print(m,A[i])