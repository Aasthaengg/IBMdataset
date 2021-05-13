import sys
from collections import Counter
import heapq


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Cnt = Counter(A)
    V = list(Cnt.values())
    heap = []
    for v in V:
        heapq.heappush(heap, -1 * v)
    if len(heap) == 1:
        print(1)
        return
    while heap:
        a = heapq.heappop(heap)
        if a == -1:
            print(-1 * sum(heap) + 1)
            return
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + 1)
        heapq.heappush(heap, b + 1)


if __name__ == "__main__":
    main()
