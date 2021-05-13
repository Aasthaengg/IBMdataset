# https://atcoder.jp/contests/abc051/tasks/abc051_b
from collections import defaultdict
k, s = map(int, input().split())

d = defaultdict(int)
for x in range(k + 1):
    for y in range(k + 1):
        d[x + y] += 1

ans = 0
for z in range(k + 1):
    ans += d.get(s - z, 0)
print(ans)