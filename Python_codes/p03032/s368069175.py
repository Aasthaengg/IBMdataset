N,K = map(int,input().split())
V = list(map(int,input().split()))
import heapq 
m = min(N,K)
M = 0
for i in range(m+1):
    for j in range(m-i+1):
        v1 = V[:i]
        v3 = V[N-j:]
        v = v1+v3
        heapq.heapify(v)
        h = K - len(v)
        while v  and h >0:
            q = heapq.heappop(v)
            h-=1
            if q > 0:
                heapq.heappush(v,q)
                break
        tmp = sum(v)
        # print(v,v3)
        M = max(M,tmp)
print(M)