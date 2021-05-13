import heapq

n,m = map(int,input().split())

a = list(map(int,input().split()))

a = [-1*i for i in a]

heapq.heapify(a)

count = 0

while count < m:
    item = heapq.heappop(a)
    item= abs(item)
    discount_item = item//2
    heapq.heappush(a,-1*discount_item)
    count += 1

print(abs(sum(a)))