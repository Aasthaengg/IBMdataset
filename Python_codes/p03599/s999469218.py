
import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    A, B, C, D, E, F = read_values()
    W = set()
    
    for a in range(F // (A * 100) + 1):
        for b in range(F // (B * 100) + 1):
            w = a * 100 * A + b * 100 * B
            if 0 < w <= F:
                W.add(w)

    S = set()
    for c in range(F // C + 1):
        for d in range(F // D + 1):
            s = c * C + d * D
            if 0 <= s <= F:
                S.add(s)
    S = sorted(list(S))
    
    s, t = 0, 100 * A
    for w in W:
        p = min(F - w, math.ceil(E * w / 100))
        f = S[bisect.bisect_right(S, p) - 1]
        if f * 100 > E * w:
            continue

        if s * (w + f) < t * f:
            s, t = f, w + f
    print(t, s)


if __name__ == "__main__":
    main()
