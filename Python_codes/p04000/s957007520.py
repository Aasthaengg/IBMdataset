from collections import Counter
from collections import defaultdict as dd

h, w, n = map(int, input().split())
d = dd(int)

for _ in range(n):
  a, b = map(int, input().split())
  for i in range(3):
    for j in range(3):
      if a-i>0 and b-j>0 and a-i<=h-2 and b-j<=w-2:
        d[(a-i, b-j)] += 1
d = dict(d)
con = Counter(d.values())
con[0] = (h-2)*(w-2) - sum(con.values())
for i in range(10):
  print(con[i])