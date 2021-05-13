
from collections import Counter
from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(M)]

pq = []
ctr = Counter(A)
for val, cnt in ctr.items():
    heappush(pq, (-val, cnt))

for b, c in X:
    heappush(pq, (-c, b))

cnt = 0
ans = 0
while cnt < N:
    val, c = heappop(pq)
    ans += val * min(c, N - cnt)
    cnt += c

print(-ans)
