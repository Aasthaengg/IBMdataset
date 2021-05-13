
from collections import defaultdict
from bisect import bisect_right

S = input()
T = input()

ctr = defaultdict(list)
for i, s in enumerate(S):
    ctr[s].append(i)

i = -1
cnt = 0
flag = False
for t in T:
    if t not in ctr:
        flag = True
        break

    j = bisect_right(ctr[t], i)
    if j == len(ctr[t]):
        idx = ctr[t][0]
    else:
        idx = ctr[t][j]

    if i >= idx:
        cnt += 1
    i = idx

if flag:
    print(-1)
else:
    print(cnt * len(S) + i + 1)
