import heapq
import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

B = [-A[i] for i in range(N)]
heapq.heapify(B)
while M:
    p = heapq.heappop(B)
    p /= 2
    heapq.heappush(B, p)
    M -= 1

ans = 0
for i in range(N):
    ans += math.floor(-B[i])
print(ans)
