def abc141d():
    import heapq
    n, m = map(int, input().split())
    a = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(a)
    for _ in range(m):
        v = -heapq.heappop(a)
        v = v//2
        heapq.heappush(a, -v)
    print(abs(sum(a)))

abc141d()