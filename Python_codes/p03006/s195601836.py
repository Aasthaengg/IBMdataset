from operator import itemgetter
from collections import defaultdict
n = int(input())
if n == 1:
  print(1)
  exit()
xy = sorted([list(map(int, input().split())) for i in range(n)], key = itemgetter(0,1))
a = defaultdict(int)
for key,(x1,y1) in enumerate(xy):
  for x2,y2 in xy[key+1:]:
    p,q = x2-x1, y2-y1
    if p != 0 or q != 0:
      a[(p,q)] += 1
ans = n - max(a.values())
print(ans)