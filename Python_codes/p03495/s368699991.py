import sys
from collections import defaultdict
from heapq import *
def input(): return sys.stdin.readline().strip()


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A: d[a] += 1
    q = []
    for key in d: heappush(q, -d[key])
    for _ in range(k):
        if q: heappop(q)
    print(-sum(q))


if __name__ == "__main__":
    main()
