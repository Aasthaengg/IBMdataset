from itertools import accumulate
from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = [0] + [x % M for x in accumulate(A)]
print(sum(x * (x - 1) // 2 for x in Counter(C).values()))