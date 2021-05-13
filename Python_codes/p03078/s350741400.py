import heapq
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
q = [[(A[0]+B[0]+C[0])*-1, 0, 0, 0]]
heapq.heapify(q)
used = {}
for i in range(K):
    if len(q) == 0:
        break
    a, b, c, d = heapq.heappop(q)
    print(a*(-1))
    if (b+1, c, d) in used:
        pass
    elif b+1 < X:
        heapq.heappush(q, [(A[b+1]+B[c]+C[d])*(-1), b+1, c, d])
        used[(b+1, c, d)] = 1
    if (b, c+1, d) in used:
        pass
    elif c+1 < X:
        heapq.heappush(q, [(A[b]+B[c+1]+C[d])*(-1), b, c+1, d])
        used[(b, c+1, d)] = 1
    if (b, c, d+1) in used:
        pass
    elif d+1 < X:
        heapq.heappush(q, [(A[b]+B[c]+C[d+1])*(-1), b, c, d+1])
        used[(b, c, d+1)] = 1
