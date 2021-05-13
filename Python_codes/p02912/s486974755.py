import heapq
def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(map(lambda x: x*(-1), a))

    heapq.heapify(a)
    cnt = 0
    while cnt < m:
        x = heapq.heappop(a)
        heapq.heappush(a, -(-x//2))
        cnt += 1
        if x == 0: break

    return sum(a)*(-1)

print(solve())