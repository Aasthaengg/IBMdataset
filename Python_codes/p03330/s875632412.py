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
    n, m = getList()
    g = []
    for i in range(m):
        g.append(getList())
    # print(g)
    ll = [defaultdict(int) for i in range(3)]

    for i in range(n):
        l = getZList()
        for j, nn in enumerate(l):
            ll[(i+j) % 3][nn] += 1
    # print(ll)
    ans = INF
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            for k in range(m):
                if i == k or j == k:
                    continue
                tmp = 0
                for kk, vv in ll[0].items():
                    tmp += g[kk][i] * vv
                for kk, vv in ll[1].items():
                    tmp += g[kk][j] * vv
                for kk, vv in ll[2].items():
                    tmp += g[kk][k] * vv
                    # print(tmp)
                # print(i, j, k, tmp)
                ans = min(ans, tmp)

    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()