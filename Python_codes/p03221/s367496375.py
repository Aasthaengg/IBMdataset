import bisect
from collections import defaultdict
n, m = map(int, input().split())
dic = defaultdict(lambda : [])
cities = []
for _ in range(m):
    p, y = map(int, input().split())
    cities.append((p, y))
    dic[p].append(y)
for key, vals in dic.items():
    dic[key] = sorted(vals)
for p, y in cities:
    pos = bisect.bisect_right(dic[p], y)
    print('{:06}{:06}'.format(p, pos))