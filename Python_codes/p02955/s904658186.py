from heapq import heappush, heappop


N, K = map(int, input().split())
A = list(map(int, input().split()))

divs = []
maxA = sum(A)
for i in range(1, int(maxA ** 0.5) + 1):
    if maxA % i == 0:
        heappush(divs, -i)
        j = maxA // i
        if i != j:
            heappush(divs, -j)

while True:
    d = -heappop(divs)
    q = []
    asum = 0
    for a in A:
        rest = a % d
        asum += rest
        heappush(q, -rest)
    cnt = 0
    for i in range(asum // d):
        cnt += d - (-heappop(q))
    if cnt <= K:
        print(d)
        exit()
