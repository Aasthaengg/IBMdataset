from heapq import heappush, heappop

h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]

nums = []
for _ in range(h):
    nums += [int(i) for i in input().split()]


def dijkstra(s=1, c=c):
    INF = float('inf')

    d = {i: INF for i in range(10)}
    d[-1] = 0
    d[s] = 0

    queue = []
    heappush(queue, (0, s))

    while queue:
        di, v = heappop(queue)
        for i in range(10):
            dtmp = d[v] + c[i][v]
            if dtmp < d[i]:
                d[i] = dtmp
                heappush(queue, (dtmp, i))

    return d


magic = dijkstra()
answer = sum(magic[i] for i in nums)
print(answer)
