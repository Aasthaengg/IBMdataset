from heapq import heapify, heappop, heappush


K, T, *A = map(int, open(0).read().split())
pq = [(-a, i) for i, a in enumerate(A)]
heapify(pq)

ans = 0
prev = -1
for _ in range(K):
    v, k = heappop(pq)
    if v == 0:
        heappush(pq, (v, k))
        ans += 1
    elif k != prev:
        prev = k
        heappush(pq, (v + 1, k))
    elif len(pq) > 1 and pq[0][0] < 0:
        v_nx, k_nx = heappop(pq)
        prev = k_nx
        heappush(pq, (v_nx + 1, k_nx))
        heappush(pq, (v, k))
    else:
        ans += 1
        heappush(pq, (v + 1, k))
print(ans)
