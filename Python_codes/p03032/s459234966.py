from collections import deque
from heapq import heappush, heappop
from copy import deepcopy

n, k = map(int, input().split())
v = list(map(int, input().split()))

dq = deque(v)

ans = 0
for ab in range(k + 1):
    cd = k - ab
    for a in range(ab + 1):
        hp = []
        cp = deepcopy(dq)

        b = ab - a
        for _ in range(a):
            if cp:
                val = cp.popleft()
                heappush(hp, val)
        for _ in range(b):
            if cp:
                val = cp.pop()
                heappush(hp, val)

        for _ in range(cd):
            if not hp or hp[0] >= 0:
                break
            heappop(hp)

        ans = max(ans, sum(hp))

print(ans)
