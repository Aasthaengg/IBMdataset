import sys
def input(): return sys.stdin.readline().rstrip()
import heapq

N, M = map(int,input().split())
A = list(map(lambda x:int(x) * (-1),input().split()))
heapq.heapify(A)

for i in range(M):
    a = heapq.heappop(A)
    a *= -1
    a //= 2
    a *= -1    
    heapq.heappush(A,a)

print(-sum(A))
