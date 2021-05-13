from collections import defaultdict
d = defaultdict(int)
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
xy.sort()

for i in range(n - 1):
    xa, ya = xy[i]
    for j in range(i + 1, n):
        xb, yb = xy[j]
        p = xb - xa
        q = yb - ya
        d[(p, q)] += 1

ans = n
for k, v in d.items():
    ans = min(ans, n - v)
if n == 1:
    ans = 1

print(ans)
