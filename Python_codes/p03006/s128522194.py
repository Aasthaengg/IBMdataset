import sys
from collections import Counter

readline = sys.stdin.readline
n = int(readline())
xy = [list(map(int, readline().split())) for _ in range(n)]

d = []
for i in range(n-1):
    for j in range(i+1, n):
        p = xy[i][0] - xy[j][0]
        q = xy[i][1] - xy[j][1]
        d.append((p, q))
        d.append((-p, -q))

if n > 1:
    ans = n - max(Counter(d).values())
else:
    ans = 1

print(ans)
