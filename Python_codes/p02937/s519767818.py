from collections import defaultdict
import bisect

S = input()
T = input()
d = defaultdict(list)
for i, s in enumerate(S):
    d[s].append(i)

x = -1
cnt = 0

for t in T:
    if len(d[t]) == 0:
        print(-1)
        exit()
    y = bisect.bisect_right(d[t], x)
    if y == len(d[t]):
        cnt += 1
        x = d[t][0]
    else:
        x = d[t][y]

ans = len(S) * cnt + x + 1
print(ans)