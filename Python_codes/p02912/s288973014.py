n,m=map(int, input().split())
a=[int(x) for x in input().split()]
a=[-1*x for x in a]

import heapq

heapq.heapify(a)

for i in range(m):
    max_value = heapq.heappop(a) #最大値の取得
    heapq.heappush(a, (max_value/2)) #半額にして-1倍してからキューに戻す

a=[-1*x for x in a]
a=[int(x) for x in a]
print(sum(a))