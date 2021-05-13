import heapq

K, T = map(int, input().split())

hp = []
heapq.heapify(hp)
for i in input().split():
    heapq.heappush(hp, -int(i))

pre = -heapq.heappop(hp) - 1  
while hp:
    q = -heapq.heappop(hp)
    if pre > 0:
        heapq.heappush(hp, -pre)
    pre = q - 1
print(pre)
