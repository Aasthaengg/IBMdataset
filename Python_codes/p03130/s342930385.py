from collections import Counter
from itertools import chain
from sys import stdin
d = Counter(chain.from_iterable([list(map(int, stdin.readline().rstrip().split())) for _ in range(3)]))
if d[1] <= 2 and d[2] <= 2 and d[3] <= 2 and d[4] <= 2:
    print('YES')
else:
    print('NO')