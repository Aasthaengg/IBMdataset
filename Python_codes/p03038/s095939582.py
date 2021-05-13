n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]


import heapq
aa = a.copy()
heapq.heapify(aa)

f = False
bc.sort(key=lambda x:x[1], reverse=True)
for b, c in bc:
    for _ in range(b):
        x = heapq.heappop(aa)
        if x < c:
            heapq.heappush(aa, c)
        else:
            heapq.heappush(aa, x)
            f = True
            break
    if f:
        break

print(sum(aa))
