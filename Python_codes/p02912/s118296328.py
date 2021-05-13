N,M=list(map(int,input().split()))
import sys
A= list(map(int,sys.stdin.readline().split()))
A=[i*-1 for i in A]
import heapq
heapq.heapify(A)
for i in range(M):
    X=heapq.heappop(A)
    X=abs(X)//2*-1
    heapq.heappush(A,X)
print(abs(sum(A)))