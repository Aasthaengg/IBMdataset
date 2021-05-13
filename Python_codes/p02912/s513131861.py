# 優先度付キューのimport
import heapq

n, m = map(int, input().split())

a = [int(i) * -1 for i in input().split()]

heapq.heapify(a)

for i in range(m):
    minPrice = heapq.heappop(a)
    # 負の切捨てが面倒なので正の値にしてからまた負に戻す
    minPrice = -(abs(minPrice) // 2)
    heapq.heappush(a, minPrice)

sum = 0
for i in a:
    sum += -i

print(sum)