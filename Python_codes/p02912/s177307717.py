import heapq

N, M = map(int, input().split())
A = [-int(x) for x in input().split()]
heapq.heapify(A)
for _ in range(M):
    pop = heapq.heappop(A)
    if pop % 2 == 0:
        num = pop//2
    else:
        num = (pop+1)//2
    heapq.heappush(A, num)

print(-sum(A))
