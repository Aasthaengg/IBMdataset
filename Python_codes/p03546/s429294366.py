import sys
from collections import defaultdict
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()


def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]

    cost = [10**18] * 10
    cost[1] = 0
    q = [(0, 1)]
    while q:
        c, u = heappop(q)
        if c > cost[u]: continue
        for i in range(10):
            if i == u: continue
            if c + C[i][u] < cost[i]:
                cost[i] = cost[u] + C[i][u]
                heappush(q, (cost[i], i))
    
    d = defaultdict(int)
    for _ in range(H):
        A = list(map(int, input().split()))
        for a in A: d[a] += 1
    ans = 0
    for i in range(10): ans += cost[i] * d[i]
    print(ans)


if __name__ == "__main__":
    main()
