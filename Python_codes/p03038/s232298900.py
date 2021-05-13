from collections import defaultdict
from collections import Counter

n, m = map(int, input().split())
arr = list(map(int, input().split()))

d = defaultdict(int)
c = Counter(arr)

for k, v in c.items():
    d[k] += v

for _ in range(m):
    b, c = map(int, input().split())
    d[c] += b

d = list(d.items())
d.sort(key=lambda x: x[0], reverse=True)

ans = 0
for k, v in d:
    ans += k * min(n, v)
    if n > v:
        n -= v
    else:
        break

print(ans)