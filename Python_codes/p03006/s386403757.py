import itertools
from collections import defaultdict

n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))
    
dd = defaultdict(int)
for lst in itertools.combinations(xy, 2):
    dx = lst[0][0] - lst[1][0]
    dy = lst[0][1] - lst[1][1]
    dd[(dx, dy)] += 1
    dd[(-dx, -dy)] += 1
ans = 0
for i, j in dd.items():
    ans = max(ans, j)
print(n - ans)