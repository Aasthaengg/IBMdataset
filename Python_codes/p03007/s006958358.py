import sys
import collections as col
import bisect
import numpy as np


def main():
    n = int(input())
    aarray = [int(e) for e in input().split()]
    aarray.sort()
    record = []
    endpoint = max(1, bisect.bisect(aarray, 0))
    aqueue = col.deque(aarray)
    while len(aqueue) > endpoint + 1:
        amax = aqueue.pop()
        amin = aqueue.popleft()
        record.append((amin, amax))
        aqueue.appendleft(amin - amax)
    amax = aqueue.pop()
    while len(aqueue) > 0:
        amin = aqueue.popleft()
        record.append((amax, amin))
        amax -= amin
    print(amax)
    for r in record:
        print(r[0], r[1])


main()
