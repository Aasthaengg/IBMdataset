#!/usr/bin/env python
import sys
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def main():
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())

    N, K = map(int, input().split())
    S = input().strip()

    count = 0
    for i in range(len(S)):
        s = S[i]
        if s == 'L' and i > 0:
            if S[i-1] == 'L':
                count += 1
        if s == 'R' and i < len(S) - 1:
            if S[i+1] == 'R':
                count += 1

    state = None
    for i in range(len(S)):
        s = S[i]
        if state is None:
            state = s
            continue
        if len(state) == 1:
            if state != s:
                state += s
        else:
            if (state == 'RL' and s == 'R') or (state == 'LR' and s == 'L'):
                count += 2
                state = s
                K -= 1
                if K == 0:
                    break

    if K > 0 and (state == 'RL' or state == 'LR'):
        count += 1

    print(count)

if __name__ == '__main__':
    main()
