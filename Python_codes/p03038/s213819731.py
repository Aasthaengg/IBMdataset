import heapq
from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
hq = []
heapq.heapify(hq)
for i in range(N):
    d[A[i]] += 1

for key, value in d.items():
    heapq.heappush(hq, (-key, value))

for i in range(M):
    b, c = map(int, input().split())
    heapq.heappush(hq, (-c, b))

ans = 0
for i in range(N):
    number, cnt = heapq.heappop(hq)
    ans += number
    if cnt > 1:
        heapq.heappush(hq, (number, cnt-1))

print(-ans)

