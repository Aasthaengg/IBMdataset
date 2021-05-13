import sys
import math
import copy
import random
import itertools
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 21
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def solve(n=None, s1=None, s2=None):
    n, k = getList()
    pli = getList()
    cli = getList()

    ans = max(cli)
    for i in range(n):
        cycle = [i]
        pts = [cli[i]]
        pos = i
        while True:
            pos = pli[pos] - 1
            if pos != i:
                cycle.append(pos)
                pts.append(cli[pos])
            else:
                break
        lc = len(cycle)
        acc = 0
        sumpts = sum(pts)
        for j in range(lc):
            acc += pts[j]

            if sumpts > 0:
                around = (k - j - 1) // lc
                tmp = acc + sumpts * around
            else:
                tmp = acc
            ans = max(ans, tmp)

    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
    return


if __name__ == "__main__":
    # main()
    solve()

