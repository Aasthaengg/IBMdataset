N ,M = map(int, input().split())
A_list = [int(i) * (-1) for i in input().split()]


import heapq

heapq.heapify(A_list)
for i in range(M):
    x = heapq.heappop(A_list)
    heapq.heappush(A_list, (-1)*(-x//2))

print(-sum(A_list))