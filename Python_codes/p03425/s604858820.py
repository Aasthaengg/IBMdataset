from collections import Counter
from itertools import combinations
n = int(input())
s = []
for _ in range(n):
  t = input()[0]
  if t in {"M","A","R","C","H"}:
    s.append(t)

count = Counter(s)
if len(count) < 3:
  print(0)
  exit()

nums = []
for i in count.values():nums.append(i)

ans = 0
for i in combinations(nums, 3):
  ans += i[0]*i[1]*i[2]
print(ans)