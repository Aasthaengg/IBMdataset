N,K = map(int,input().split())
V = list(map(int,input().split()))

import heapq
ans = 0
for a in range(min(N,K)+1):
    for b in range(min(N,K)-a+1):
        A = V[:a] + V[N-b:]
        heapq.heapify(A)
        for c in range(min(a+b, K-a-b)):
            small = heapq.heappop(A)
            if small > 0:
                heapq.heappush(A,small)
                break
        ans = max(ans, sum(A))
print(ans)
