import sys
import math
import copy
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

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def solve():
    n,C = getList()
    li = []

    start = [[0] * 100100 for i in range(31)]
    end = [[0] * 100100 for i in range(31)]
    pt = [0] * 100100

    for i in range(n):
        s, t, c = getList()
        start[c][s] += 1
        end[c][t] += 1
        pt[s] += 1
        pt[t+1] -= 1

    for i in range(100099):
        pt[i+1] += pt[i]

    ans = 0
    for i in range(100100):
        tmp = pt[i]
        for j in range(31):
            if start[j][i] and end[j][i]:
                tmp -= 1
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
