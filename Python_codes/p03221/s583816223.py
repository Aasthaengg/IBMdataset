import bisect
from collections import defaultdict

N, M = map(int, input().split(' '))
cities = []
years = defaultdict(list)
for _ in range(M):
    p, y = map(int, input().split(' '))
    cities.append((p, y))
    years[p].append(y)

for p in years.keys():
    years[p].sort()

for p, y in cities:
    print('{:06}{:06}'.format(p, bisect.bisect_right(years[p], y)))
