import heapq

n, m = map(int,input().split())
a = [-1 * int(i) for i in input().split()]

ans = 0

heapq.heapify(a)

for i in range(m):
    hangaku = (heapq.heappop(a) * -1) // 2 * -1
    heapq.heappush(a, hangaku)    

print(-1*sum(a))