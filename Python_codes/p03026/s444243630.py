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


def dfs(L, v, p, D):
    for w in L[v]:
        if w == p:
            continue
        dfs(L, w, v, D)
    D.append(v)


def main():
    N = int(input())
    L = [set() for _ in range(N)]
    for _ in range(N - 1):
        a, b = read_index()
        L[a].add(b)
        L[b].add(a)
    
    C = read_list()
    C.sort()

    D = []
    dfs(L, 0, -1, D)
    E = [""] * N
    for i, d in enumerate(D):
        E[d] = str(C[i])
    
    print(sum(C[: N - 1]))
    print(" ".join(E))


if __name__ == "__main__":
    main()