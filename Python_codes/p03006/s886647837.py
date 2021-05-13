from itertools import combinations
from collections import Counter

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

cXY = combinations(XY, 2)

edge = []
for a, b in cXY:
  edge.append((a[0]-b[0], a[1]-b[1]))
  edge.append((-a[0]+b[0], -a[1]+b[1]))

ce = Counter(edge)

if N == 1:
  ans = 1
else:
  dup = max(ce.values())
  ans = N - dup
print(ans)