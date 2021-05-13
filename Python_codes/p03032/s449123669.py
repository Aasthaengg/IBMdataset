import heapq 

N,K = map(int,input().split())
A = list(map(int,input().split()))
m = min(N,K) #KがNより大きい場合を防ぐ
M = 0 
for i in range(m+1):
    for j in range(m-i+1):
        A1 = A[:i]
        A3 = A[N-j:]
        new_A = A1+A3
        heapq.heapify(new_A)
        h = K - len(new_A)
        while new_A  and h >0:
            q = heapq.heappop(new_A)
            h-=1
            if q > 0:
                heapq.heappush(new_A,q)
                break
        M = max(M,sum(new_A))
print(M)