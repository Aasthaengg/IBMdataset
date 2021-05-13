from collections import Counter, deque
from bisect import *
alphabets = list("abcdefghijklmnopqrstuvwxyz")
s = input()
t = input()
cs = Counter(list(s))
ct = Counter(list(t))
for char in alphabets:
    if ct[char] > 0 and cs[char]==0:
        print(-1)
        exit()

l_s = len(s)
l_t = len(t)
ss = list(s+s)
c2loc = {char: [] for char in alphabets}
for i in range(l_s*2):
    c2loc[ss[i]].append(i)

ans = 0
now = -1
for i in range(l_t):
    target = t[i]
    target_idxes = c2loc[target]
    idx = bisect_right(target_idxes, now)
    ans += target_idxes[idx] - now
    now = target_idxes[idx]%l_s
print(ans)