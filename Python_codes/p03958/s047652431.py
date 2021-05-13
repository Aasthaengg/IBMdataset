#https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_b

import heapq

k, t = list(map(int, input().split()))
cakes = list(map(lambda x: int(x)*-1, input().split()))
heapq.heapify(cakes)
ans = 0
top_change = True
for i in range(k):
    if top_change:
        first = heapq.heappop(cakes)
        first += 1
        if len(cakes) == 0:
            ans += first*-1
            break
        if first < cakes[0]:
            top_change = False
        else:
            top_change = True
        if first != 0:
            heapq.heappush(cakes, first)
    else:
        first = heapq.heappop(cakes)
        second = heapq.heappop(cakes)
        second += 1
        heapq.heappush(cakes, first)
        if second != 0:
            heapq.heappush(cakes, second)
        top_change = True

print(ans)

