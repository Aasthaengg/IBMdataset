import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
heapq.heapify(A)

BC = [list(map(int, input().split())) for i in range(m)]
BC = sorted(BC,key = lambda x:-x[1])

for b,c in BC:
    for i in range(b):
        a = heapq.heappop(A)
        if a < c:
            heapq.heappush(A,c)
        else:
            heapq.heappush(A,a)
            break
print(sum(A))