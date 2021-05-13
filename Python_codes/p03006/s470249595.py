import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
xy = [tuple([int(i) for i in input().split()]) for _ in range(N)]
ary = []
if N == 1:
    print(1)
    exit()
for i, t in enumerate(xy[:-1]):
    x = t[0]
    y = t[1]
    for x2, y2 in xy[i+1:]:
        ary.append((x2-x, y2-y))
        ary.append((x-x2, y-y2))
c = dict(Counter(ary))
print(N-max(c.values()))
