#!/usr/bin/env python
import sys
import re
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def main():
    input = sys.stdin.readline
    #N, M = map(int, input().split())
    #N, K = map(int, input().split())
    #ps = list(map(int, input().split()))

    N = int(input())

    A_all = []
    for i in range(N):
        As = list(map(int, input().split()))
        A_all.append(As)
    A_index = [0] * N

    candidates = set(range(1, N+1))
    for i in range(N * (N - 1) // 2 + 1):
        matches = set()
        for j in candidates:
            A_idx = A_index[j - 1]
            if A_idx >= N - 1:
                continue
            k = A_all[j - 1][A_idx]
            B_idx = A_index[k - 1]
            if B_idx >= N - 1:
                continue
            if j == A_all[k - 1][B_idx]:
                pair = tuple(sorted([j, k]))
                matches.add(pair)

        if not matches:
            break

        candidates = set()
        for match in matches:
            for j in match:
                A_index[j - 1] += 1
                candidates.add(j)

    if all([A_idx == N - 1 for A_idx in A_index]):
        print(i)
    else:
        print(-1)


if __name__ == '__main__':
    main()
