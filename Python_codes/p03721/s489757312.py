n,k = list(map(int, input().split()))
ab = sorted([tuple(map(int, input().split())) for _ in range(n)])
A,B = list(zip(*ab))

from itertools import accumulate
import bisect
print(A[bisect.bisect_left(list(accumulate(B)), k)])
