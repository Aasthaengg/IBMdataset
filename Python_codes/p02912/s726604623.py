import heapq
n,m = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))
heapq.heapify(A)

while m > 0:
    x = heapq.heappop(A)*(-1)
    x //= 2
    A.append(-x)
    m -= 1
print(abs(sum(list(A))))