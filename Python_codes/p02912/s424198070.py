import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))
heapq.heapify(A)

for _ in range(M):
    a = ((heapq.heappop(A)*-1)//2)*-1
    if a != 0:
        heapq.heappush(A, a)

    if len(A) == 0:
        break

print(sum(A)*-1)
