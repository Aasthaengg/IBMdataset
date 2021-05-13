#!/usr/bin/env python
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor

def main():
    #N, M = map(int, input().split())
    N, M = map(int, input().split())

    As = list(map(int, input().split()))
    As = sorted(As)
    """
    queue = deque()
    for i in range(N):
        a = As[i]
        pos = bisect.bisect_left(queue, a)
        queue.insert(pos, a)
    """

    B_C = []
    for i in range(M):
        B, C = map(int, input().split())
        B_C.append((B, C))

    B_C = sorted(B_C, key=lambda x: x[1], reverse=True)

    total = 0
    for B, C in B_C:
        for i in range(B):
            if not As or C <= As[0]:
                break
            As.pop(0)
            total += C

    if As:
        total += sum(As)

    print(total)


if __name__ == '__main__':
    main()
