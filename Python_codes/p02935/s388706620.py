import heapq
N = int(input())
Nlist = list(map(int, input().split()))
heapq.heapify(Nlist)
for _ in range(N-1):
    x = heapq.heappop(Nlist)
    y = heapq.heappop(Nlist)
    z = (x+y)/2
    heapq.heappush(Nlist, z)

print(Nlist[0])
