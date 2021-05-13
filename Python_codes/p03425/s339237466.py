from collections import Counter
from itertools import combinations

n = int(input())
l = [input()[0] for _ in range(n)]
lc = Counter(l)

con = []
for c in 'MARCH':
  if c in lc:
    con.append(lc[c])

ans = 0
for a, b, c in combinations(con, 3):
  ans += a*b*c
  
print(ans)