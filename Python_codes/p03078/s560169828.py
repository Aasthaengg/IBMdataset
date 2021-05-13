X,Y,Z,K = map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

from collections import defaultdict
done = defaultdict(lambda:False)
import heapq
q = [(-A[0]-B[0]-C[0],0,0,0)]
heapq.heapify(q)

for _ in range(K):
    ma,i,j,k = heapq.heappop(q)
    if not done[(i+1,j,k)] and i<X-1:
        done[(i+1,j,k)]=True
        heapq.heappush(q,(-A[i+1]-B[j]-C[k] , i+1,j,k))
    
    if not done[(i,j+1,k)] and j<Y-1:
        done[(i,j+1,k)]=True
        heapq.heappush(q,(-A[i]-B[j+1]-C[k] , i,j+1,k))
    
    if not done[(i,j,k+1)] and k<Z-1:
        done[(i,j,k+1)]=True
        heapq.heappush(q,(-A[i]-B[j]-C[k+1] , i,j,k+1))
    print(-ma)