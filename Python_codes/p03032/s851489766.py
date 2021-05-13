#!/usr/bin/env python
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor

def main():
    #N, M = map(int, input().split())
    N, K = map(int, input().split())
    Vs = list(map(int, input().split()))

    max_value = None
    for l in range(min([K+1, N+1])):
        for r in range(min([K+1-l, N-l+1])):
            for b in range(K - l - r + 1):
                values = list(Vs[:l])
                if r > 0:
                    values += list(Vs[-r:])
                values = sorted(values)
                for i in range(b):
                    if values and values[0] < 0:
                        values.pop(0)
                    else:
                        break
                value = sum(values)
                if max_value is None or max_value < value:
                    max_value = value

    print(max_value)


if __name__ == '__main__':
    main()
