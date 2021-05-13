from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
A = list(map(lambda x: -int(x), input().split()))
if N == 1:
    print(N >> M)
    exit()
heapify(A)
while M > 0:
    a = -heappop(A)
    while M > 0 and a >= -A[0]:
        a >>= 1
        M -= 1
    heappush(A, -a)
print(-sum(A))