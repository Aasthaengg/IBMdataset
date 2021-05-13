def resolve():
    N, M = list(map(int, input().split()))
    A = list(map(lambda x: -int(x), input().split()))
    import heapq
    heapq.heapify(A)
    for i in range(M):
        v = heapq.heappop(A)
        heapq.heappush(A, v/2)
    import math
    A = list(map(lambda x: math.floor(-x), A))
    print(sum(A))
    


if '__main__' == __name__:
    resolve()