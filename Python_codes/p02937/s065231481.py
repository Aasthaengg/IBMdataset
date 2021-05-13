from collections import defaultdict
from bisect import bisect_left
S = input()
sl = len(S)
T = input()
t = set(T)
dic = defaultdict(list)
for c in t:
  for i, m in enumerate(S):
    if m==c:
      dic[c] += [i]
  if dic[c]==[]:
    print(-1)
    import sys
    sys.exit()
p = -1
ans = 0
pc = ''
for c in T:
  if pc==c:
    p += 1
    ans += 1
  if p>dic[c][-1]:
    ans += sl-1-p
    p = -1
  ind = bisect_left(dic[c],p)
  ans += dic[c][ind]-p
  p = dic[c][ind]
  pc = c
print(ans)