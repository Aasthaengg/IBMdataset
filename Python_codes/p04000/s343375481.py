from itertools import product
from collections import defaultdict, Counter
import sys
input = sys.stdin.readline
h,w,n = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
pls = defaultdict(int)
for x,y in a:
  for arx,ary in product(list(range(x-1,x+2)),list(range(y-1,y+2))):
    if 2<=arx<=h-1 and 2<=ary<=w-1:
      pls[(arx,ary)] += 1
c = Counter(pls.values())
print((h-2)*(w-2)-sum(c.values()))
for i in range(1,10):
  print(c[i])
