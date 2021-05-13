from collections import defaultdict
from bisect import bisect_right

s = input()
t = input()

indices = defaultdict(list)
for i, v in enumerate(s):
    indices[v].append(i)

cnt = 0
cur = -1
mod = len(s)
flag = False
for v in t:
    if v not in indices:
        flag = True
        break

    i = bisect_right(indices[v], cur)
    if i == len(indices[v]):
        j = indices[v][0]
    else:
        j = indices[v][i]

    if cur >= j:
        cnt += 1
    cur = j

if flag:
    print(-1)
else:
    print(cnt * mod + cur + 1)
