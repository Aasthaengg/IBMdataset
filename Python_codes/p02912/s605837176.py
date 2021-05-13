import heapq

n,m = map(int,input().split())
a = list(map(lambda x: -int(x),input().split()))
heapq.heapify(a)
for _ in range(m):
    temp = -heapq.heappop(a)
    temp//=2
    heapq.heappush(a,-temp)
ans = 0
for _ in range(n):
    ans -= heapq.heappop(a)
print(ans)