from itertools import accumulate
from bisect import bisect

n, m, k = map(int, input().split())
(*a,) = accumulate(map(int, input().split()))
(*b,) = accumulate(map(int, input().split()))
a = (0,) + tuple(i for i in a if i <= k)
b = tuple(i for i in b if i <= k)
print(max(i + bisect(b, k - a[i]) for i in range(len(a))))