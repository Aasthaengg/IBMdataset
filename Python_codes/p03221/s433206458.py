from collections import defaultdict
import bisect

pre = defaultdict(list)
ori = []
n, m = map(int, input().split())
for _ in range(m):
    x, y = map(int, input().split())
    pre[x].append(y)
    ori.append([x, y])

for key, val in pre.items():
    val.sort()

for i in range(m):
    l = pre[ori[i][0]]
    idx = bisect.bisect(l, ori[i][1])
    print(f'{ori[i][0]:06}{idx:06}')

