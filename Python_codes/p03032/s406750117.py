from collections import deque
from heapq import heappush, heappop
n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
for i in range(n + 1):
    for j in range(n + 1):
        rest = k - i - j
        if i + j > n or rest < 0:
            continue
        tans = 0
        q = deque(v)
        poppen = []
        for _ in range(i):
            tans += q[0]
            heappush(poppen, q.popleft())
        for _ in range(j):
            tans += q[-1]
            heappush(poppen, q.pop())
        for _ in range(rest):
            if not poppen or poppen[0] >= 0:
                break
            tans -= heappop(poppen)
        ans = max(ans, tans)
print(ans)
