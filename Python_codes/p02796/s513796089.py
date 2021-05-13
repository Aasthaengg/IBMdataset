import sys
from collections import deque, Counter, defaultdict
from itertools import permutations
import heapq


def resolve():
    N = int(sys.stdin.readline().strip())
    pq = []
    for _ in range(N):
        X, L = map(int, sys.stdin.readline().strip().split())
        heapq.heappush(pq, (X + L, X - L))
    ans = 0
    while pq:
        ans += 1
        right, _ = heapq.heappop(pq)
        if pq:
            _, next_left = pq[0]
            while next_left < right:
                heapq.heappop(pq)
                if not pq:
                    break
                _, next_left = pq[0]

    print(ans)


if __name__ == "__main__":
    resolve()
