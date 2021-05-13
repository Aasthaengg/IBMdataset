import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def solve():
    x, y, z, k = getList()
    an = getList()
    bn = getList()
    cn = getList()

    ans = []
    for aa in an:
        for bb in bn:
            ans.append(aa + bb)

    ans.sort(reverse=True)
    ans = ans[:k]
    anans = []
    for aa in ans:
        for bb in cn:
            anans.append(aa + bb)

    anans.sort(reverse=True)
    for aaa in anans[:k]:
        print(aaa)

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





