n, m = map(int, input().split())

from collections import defaultdict

cb = defaultdict(int)

for a in input().split():
    cb[int(a)] += 1

for _ in range(m):
    b, c = map(int, input().split())
    cb[c] += b

cbl = sorted(cb.items())

res = n

ans = 0

while res > 0:
    c, b = cbl.pop()
    ncount = min(res, b)
    ans += c * ncount
    res -= ncount

print(ans)