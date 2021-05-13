import heapq

k = int(input())
n = 50
div = k//50
mod = k%50

ans = [div+n-1 for i in range(n)]
heapq.heapify(ans)

for i in range(mod):
    Min = heapq.heappop(ans)
    for j in range(n-1):
        ans[j] -= 1
    heapq.heappush(ans,Min+50)

print(n)
print(*ans)