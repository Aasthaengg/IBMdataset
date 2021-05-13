from itertools import combinations
from collections import Counter
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

count = []
for ((x1,x2),(x3,x4)) in combinations(xy, 2):
    count.append((x1-x3,x2-x4))
    count.append((x3-x1,x4-x2))
    
c = Counter(count)
m = 0
for i in c.values():
    m = max(m, i)

if N == 1:
    print(1)
else:
    print(N-m)
