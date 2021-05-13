from collections import defaultdict
import bisect
s = input()
t = input()

counter = defaultdict(list)
for i,c in enumerate(s):
  counter[c].append(i)

prev = 10**10
cycle = 0
for i,c in enumerate(t):
  if c not in counter:
    print(-1)
    exit()

  idx = counter[c]
  found = bisect.bisect_right(idx, prev)

  if found >= len(idx):
    cycle += 1
    prev = idx[0]
  else:
    prev = idx[found]

print( (cycle-1)*len(s) + prev+1 )