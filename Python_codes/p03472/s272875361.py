import heapq
n, h = map(int, input().split())

hq = []
nmax = 0
for i in range(n):
    a, b = map(int,input().split())
    nmax = max(nmax, a)
    heapq.heappush(hq, -b)
heapq.heappush(hq, -nmax)

ans = 0
while h > 0:
    d = -heapq.heappop(hq)
    if d == nmax:
        ans+=max(0, (h+nmax-1)//nmax)
        break
    else:
        h -= d
        ans+=1
print(ans)