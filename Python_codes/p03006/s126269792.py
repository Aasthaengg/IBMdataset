import itertools
from collections import defaultdict
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
dd = defaultdict(int)
for xy1, xy2 in itertools.combinations(xy, 2):
    x1, y1 = xy1
    x2, y2 = xy2
    unit_vect = (x1-x2, y1-y2)
    dd[unit_vect] += 1
    unit_vect = (x2-x1, y2-y1)
    dd[unit_vect] += 1

if n == 1:
    ans = 1
else:
    ans = n-max(dd.values())
print(ans)