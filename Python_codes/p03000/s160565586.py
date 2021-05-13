import itertools
import bisect

N, X = map(int, input().split())
*L, = map(int, input().split())

A = list(itertools.accumulate(L))
print(bisect.bisect(A, X) + 1)