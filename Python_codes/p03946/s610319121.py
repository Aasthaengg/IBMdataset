import sys
from itertools import accumulate
read = sys.stdin.read

N, T, *A = map(int, read().split())
a_maximum = list(reversed(list(accumulate(A[::-1], max))[:-1]))
a = [j - i for i, j in zip(A, a_maximum)]
minimum = max(a)

print(a.count(minimum))