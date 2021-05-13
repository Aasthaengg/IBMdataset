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
    n = getN()
    li = []
    for i in range(n):
        li.append(getN())

    last = dict()
    ans = [0 for i in range(n+1)]
    ans[0] = 1
    for i in range(1, n+1):
        tgt = li[i-1]
        if i >= 2 and tgt == li[i-2]:
            last[tgt] = i
            ans[i] = ans[i-1]
            continue
        if tgt not in last:
            ans[i] = ans[i-1]
            last[tgt] = i
        else:
            ans[i] = ans[i-1] + ans[last[tgt]]
            last[tgt] = i

    print(max(ans) % MOD)


def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()
