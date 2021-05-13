def resolve():
    import heapq
    import sys
    input = sys.stdin.readline
    _, M = [int(i) for i in input().split()]
    A = [-int(i) for i in input().split()]
    heapq.heapify(A)
    for _ in range(M):
        heapq.heappush(A, -(-heapq.heappop(A) // 2))
    print(-sum(A))

resolve()
