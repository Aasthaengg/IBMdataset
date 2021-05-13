from heapq import heapify, heappop, heappush
N = int(input())
vvv = list(map(int, input().split()))
heapify(vvv)
for _ in range(N - 1):
    x = heappop(vvv)
    y = heappop(vvv)
    heappush(vvv, (x + y)/2)
print(vvv[0])
