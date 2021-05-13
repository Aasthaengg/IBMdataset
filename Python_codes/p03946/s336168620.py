import sys
from itertools import accumulate
read = sys.stdin.read

N, T, *A = map(int, read().split())
a_minimum = accumulate(A, min)
a = [i - j for i, j in zip(A, a_minimum)]
minimum = max(a)

print(a.count(minimum))