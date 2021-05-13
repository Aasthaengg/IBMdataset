from collections import defaultdict
from itertools import combinations

STR = "MARCH"

N = int(input())
s = [input() for _ in range(N)]
dd = defaultdict(int)
for i in range(N):
  dd[s[i][0]] += 1
t = tuple(dd[S]  for S in STR)
p = combinations(t,3)
ans = sum(x[0]*x[1]*x[2] for x in p)
print(ans)