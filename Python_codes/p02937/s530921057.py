s = input()
t = input()

from collections import defaultdict
pos = defaultdict(list)
for i, char in enumerate(s):
    pos[char].append(i)

from bisect import bisect_left

ans = 0
before = -1
flag = True
for char in t:
    if pos[char] == []:
        flag = False
        break

    if before > pos[char][-1]:
        ans += len(s)
        before = pos[char][0] + 1
    else:
        idx = bisect_left(pos[char], before)
        before = pos[char][idx] + 1

if flag:
    print(ans + before)
else:
    print(-1)
