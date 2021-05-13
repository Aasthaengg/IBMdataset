n, m = map(int, input().split())
pd = [list(map(int, input().split())) for _ in range(m)]

from collections import defaultdict
dict = defaultdict(list)
for i, (p, d) in enumerate(pd):
    dict[p].append((d, i))

ans = ['' for _ in range(m)]
for key in dict:
    v = dict[key]
    v.sort()

    for i, (y, idx) in enumerate(v):
        tmp = str(key).zfill(6) + str(i + 1).zfill(6)
        ans[idx] = tmp

for a in ans:
    print(a)
