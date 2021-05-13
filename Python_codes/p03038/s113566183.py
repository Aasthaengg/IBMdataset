import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter
import heapq

N, M = map(int, input().split())

A = list(map(int, input().split()))

counter_A = Counter(A)

lis = []
for v,c in counter_A.items():
    heapq.heappush(lis, (-v, c))

for i in range(M):
    b, c = map(int, input().split())
    heapq.heappush(lis, (-c, b))

cnt = 0
ans = 0    

while cnt <= N:
    v, c = heapq.heappop(lis)
    v *= -1

    if cnt + c > N:
        ans += v*(N-cnt)
        break
    else:
        ans += v*c
        cnt += c
print(ans) 