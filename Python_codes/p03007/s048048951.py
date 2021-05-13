import sys
from bisect import bisect_left
read = sys.stdin.read

N, *A = map(int, read().split())
A.sort()
zero = bisect_left(A, 0)
xy = []
for i in range(1, N - 1):
    if i < zero:
        xy.append((A[-1], A[i]))
        A[-1] -= A[i]
    else:
        xy.append((A[0], A[i]))
        A[0] -= A[i]

print(A[-1] - A[0])
for x, y in xy:
    print(x, y)
print(A[-1], A[0])