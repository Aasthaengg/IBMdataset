import itertools
from collections import defaultdict

N, W = map(int, input().split())
d = defaultdict(list)
for _ in range(N):
    w, v = map(int, input().split())
    d[w].append(v)

for i in d:
    d[i] = list(itertools.accumulate(sorted(d[i], reverse=True)))
mm = min(d)

ans = 0
for t in itertools.product(range(len(d[mm]) + 1), range(len(d[mm + 1]) + 1),
                           range(len(d[mm + 2]) + 1), range(len(d[mm + 3]) + 1)):
    if sum((mm + i) * t[i] for i in range(4)) > W:
        continue
    ans = max(ans, sum(d[mm + i][t[i] - 1] if t[i] else 0 for i in range(4)))
print(ans)
