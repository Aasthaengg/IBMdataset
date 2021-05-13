import heapq

n, m = map(int, input().split()) 
al = list(map(int, input().split())) 

al = [v*(-1) for v in al]
heapq.heapify(al)

for _ in range(m):
    p = heapq.heappop(al)
    heapq.heappush(al, ((-1)*p//2)*(-1) )

print(sum(al)*(-1))