from heapq import heapify, heappush, heappop

def divisor(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n / i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors


N, K = map(int, input().split())
A = list(map(int, input().split()))
divisors = divisor(sum(A))
for d in divisors[::-1]:
    heap = []
    s = 0
    for a in A:
        x = a // d * d - a
        heap.append(x)
        s += -x
    heapify(heap)
    n = 0
    for _ in range(s // d):
        x = heappop(heap)
        if x + d > K:
            break
        else:
            if x + d > 0:
                n += x + d
            heappush(heap, x + d)
    else:
        if sum(abs(x) for x in heap) <= 2 * K:
            print(d)
            exit()
