import sys
import heapq
K, T = map(int, input().split())
m = [-int(i) for i in input().split()]
heapq.heapify(m)

if T == 1:
    print(K-1)
    sys.exit()

while len(m) > 1:
    l = heapq.heappop(m)
    r = heapq.heappop(m)
    if r+1 != 0:
        heapq.heappush(m, l+1)
        heapq.heappush(m, r+1)
    else:
        if l+1 != 0:
            heapq.heappush(m, l+1)
if len(m) == 0:
    print(0)
else:
    print(-m[0]-1)