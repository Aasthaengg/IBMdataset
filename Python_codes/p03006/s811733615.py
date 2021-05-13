import sys
from itertools import combinations
from collections import Counter
read = sys.stdin.read

N, *xy = map(int, read().split())

if N == 1:
    print(1)
    exit()

pq = []
for (a1, b1), (a2, b2) in combinations(zip(*[iter(xy)] * 2), 2):
    p = a1 - a2
    q = b1 - b2
    pq.append((p, q))
    pq.append((-p, -q))

print(N - Counter(pq).most_common()[0][1])