from heapq import heapify, heappop, heappush

N, M = map(int, input().split())
A = []
for i in input().split():
    A.append(-int(i))
heapify(A)
for _ in range(M):
    a = -heappop(A)
    heappush(A, (a // 2) * -1)
# print('A', A)
ans = -sum(A)
print(ans)
