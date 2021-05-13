import heapq
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))
heapq.heapify(A)
for _ in range(M):
    tmp = heapq.heappop(A)*(-1)
    heapq.heappush(A, (tmp/2)*(-1))
ans = 0
for _ in range(N):
    ans += math.floor(heapq.heappop(A)*(-1))
print(ans)