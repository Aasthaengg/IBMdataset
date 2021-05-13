import sys
from bisect import bisect_left
read = sys.stdin.read

N, *A = map(int, read().split())
A.sort()
zero = bisect_left(A, 0)
xy = []
minimum = A[0]
maximum = A[-1]
for i in range(1, N - 1):
    if i < zero:
        xy.append(str(maximum) + ' ' + str(A[i]))
        maximum -= A[i]
    else:
        xy.append((str(minimum) + ' ' + str(A[i])))
        minimum -= A[i]
else:
    xy.append(str(maximum) + ' ' + str(minimum))

print(maximum - minimum)
print('\n'.join(xy))