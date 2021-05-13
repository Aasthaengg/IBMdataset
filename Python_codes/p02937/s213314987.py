from bisect import bisect_right
from collections import defaultdict

s = input()
t = input()
idx = defaultdict(list)
for i in range(len(s)):
    idx[s[i]].append(i)
num = 0
prev = -1
for c in t:
    l = len(idx[c])
    if l == 0:
        print(-1)
        exit()
    j = bisect_right(idx[c], prev)
    if j == l:
        prev = idx[c][0]
        num += 1
    else:
        prev = idx[c][j]
print(len(s) * num + prev + 1)
