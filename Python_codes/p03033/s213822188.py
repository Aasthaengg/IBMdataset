# -*- coding: utf-8 -*-
"""
E - Roadwork
https://atcoder.jp/contests/abc128/tasks/abc128_e

"""
import sys

from heapq import heappop, heappush

def solve(N, Q):
    events = []
    for _ in range(N):
        s, t, x = map(int, input().split())
        events.append((s-x, 1, x))
        events.append((t-x, -1, x))
    events.sort(reverse=True)
    D = [int(input()) for _ in range(Q)]

    blocked = set()
    ans = []
    hq = []
    for d in D:
        while events and events[-1][0] <= d:
            t, e, x = events.pop()
            if e == -1:
                blocked.discard(x)
            else:
                blocked.add(x)
                heappush(hq, x)
        if blocked:
            while hq and hq[0] not in blocked:
                heappop(hq)
            ans.append(hq[0] if hq else -1)
        else:
            ans.append(-1)
    return ans


def main(args):
    N, Q = map(int, input().split())
    ans = solve(N, Q)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main(sys.argv[1:])
