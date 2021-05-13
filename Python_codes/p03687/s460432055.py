s = str(input())

from collections import Counter
cntr = Counter(c for c in s)

ans = 100100
for ch in cntr.keys():
  len_max = max([len(arr) for arr in s.split(ch)])
  ans = min(ans, len_max)

print(ans)