
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

H, W = read_values()
P = [[False for _ in range(W)] for _ in range(H)]
F = [input().strip() for i in range(H)]

def f(h, w):
    S = deque()
    S.append((h, w))
    P[h][w] = True
    T = [0, 1]
    while S:
        h, w = S.popleft()
        for hh, ww in [(h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)]:
            if not (0 <= hh < H and 0 <= ww < W):
                continue
            if P[hh][ww]:
                continue
            if F[hh][ww] == F[h][w]:
                continue
            P[hh][ww] = True
            t = 0 if F[hh][ww] == "." else 1
            T[t] += 1
            S.append((hh, ww))
    return T[0] * T[1]


def main():
    res = 0
    for h in range(H):
        for w in range(W):
            if P[h][w] or F[h][w] != "#":
                continue
            res += f(h, w)
    print(res)
    

if __name__ == "__main__":
    main()

