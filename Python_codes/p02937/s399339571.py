from collections import defaultdict
import bisect

S = input()
T = input()

d = defaultdict(list)
for i, s in enumerate(S, start=1):
    d[s].append(i)

ans = 0
i = 0

for t in T:
    if not d[t]:
        print(-1)
        exit()

    if i >= d[t][-1]:
        ans += len(S)
        i = d[t][0]
        continue

    pos = bisect.bisect_right(d[t], i)
    i = d[t][pos]

ans += i
print(ans)
