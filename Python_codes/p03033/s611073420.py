from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

def solve():
    N, Q = map(int, input().split())
    events = []
    for i in range(N):
        S, T, X = map(int, input().split())
        events.append((S-X-0.5, 1, X))
        events.append((T-X-0.5, 0, X))
    for i in range(Q):
        D = int(input())
        events.append((D, 2, i))

    events.sort()

    anss = [-1] * Q
    PQ = []
    isClosed = dict()
    for tm, tp, x in events:
        if tp == 0:
            isClosed[x] = 0
        elif tp == 1:
            isClosed[x] = 1
            heappush(PQ, x)
        else:
            while PQ:
                if isClosed[PQ[0]] == 1:
                    anss[x] = PQ[0]
                    break
                heappop(PQ)

    print('\n'.join(map(str, anss)))


solve()
