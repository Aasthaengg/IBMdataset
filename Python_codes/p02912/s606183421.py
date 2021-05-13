import heapq
n,m = map(int,input().split())
p = list(map(int,input().split()))
price = [x*(-1) for x in p]
heapq.heapify(price)
while m != 0:
    max_price = heapq.heappop(price)*(-1)
    heapq.heappush(price,(max_price//2)*(-1))
    m -= 1
print(sum(price)*(-1))