from itertools import accumulate
from collections import Counter
N, T = map(int, input().split())
A = list(map(int, input().split()))
B = list(accumulate(A, min))
C = Counter(b-a for a, b in zip(A, B))
print(C[min(C)])