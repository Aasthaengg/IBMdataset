N, M = map(int, input().split())
A = map(int, input().split())
from itertools import accumulate
from collections import Counter
acc = [0]
acc.extend(accumulate(A))
c = Counter(ac % M for ac in acc)
print(sum(v * (v - 1) // 2 for v in c.values()))