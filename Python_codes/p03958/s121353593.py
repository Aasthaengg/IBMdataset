K,T = map(int,input().split())
from heapq import heapify, heappop, heappush
A = list(map(int,input().split()))
for i in range(T):
    A[i] = (-A[i],i)
A.append((0,999))
A.sort()
heapify(A)
ans = 0
pre = -1

for i in range(K):
    a,i = heappop(A)
    if pre != i:
        heappush(A,(a+1,i))
        pre = i
    else:
        a2,i2 = heappop(A)
        if a2 < 0:
            pre = i2
            heappush(A,(a2+1,i2))
            heappush(A,(a,i))
        else:
            ans += 1
            heappush(A,(a+1,i))
            heappush(A,(a2,i2))
print(ans)

    


