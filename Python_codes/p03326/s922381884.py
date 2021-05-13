import heapq
from itertools import product
def resolve():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(n)]

    ans = 0

    if m == 0:
        print(0)
        return 

    for i in product([1, -1], repeat=3):
        hq = []
        heapq.heapify(hq)
        for x, y, z in cakes:
            point = i[0] * x + i[1] * y + i[2] * z
            if len(hq) != m:
                heapq.heappush(hq, point)
            elif hq[0] < point:
                heapq.heapreplace(hq, point)

        ans = max(ans, sum(hq))

    print(ans)
    
resolve()