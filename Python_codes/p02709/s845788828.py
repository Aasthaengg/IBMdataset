from heapq import heappop, heappush
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

hp = []
for i, e in enumerate(a, 1):
    heappush(hp, [-e, i])

dp = defaultdict(int)
dp[(0, n + 1)] = 0
while hp:
    e, i = heappop(hp)
    e = -e
    dp2 = defaultdict(int)
    for k, v in dp.items():
        l, r = k
        dp2[(l + 1, r)] = max(dp2[(l + 1, r)], v + abs(l + 1 - i) * e)
        dp2[(l, r - 1)] = max(dp2[(l, r - 1)], v + abs(r - 1 - i) * e)

    dp = dp2

ans = max(dp.values())

print(ans)
