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

class BIT():
    # A1 ... AnのBIT(1-indexed)
    def __init__(self, n):
        self.n = n
        self.BIT = [0] * (n + 2)

    # A1 ~ Aiまでの和 O(logN)
    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def update(self, idx, x):
        # print(idx)
        while idx <= self.n:
            # print(idx)
            self.BIT[idx] += x
            idx += idx & (-idx)
        return

    def show(self):
        print(self.BIT)

def cost(id, div, x):
    n = len(div)
    use = []
    for i in range(n):
        if id % 2 == 1:
            use.append(div[i])
        id //= 2

    return (len(use) - 1) * 10 + abs(x - sum(use))


def eachtake(div, x):
    n = len(div)
    ret = INF

    for id in range(1, 1 << n):
        tmp = cost(id, div, x)
        ret = min(tmp, ret)

    return ret


def eachpat(pat, a, b, c, li, n):
    div = [[] for i in range(3)]
    for i in range(n):
        if pat % 4 != 3:
            div[pat%4].append(li[i])
        pat //= 4

    for i in range(3):
        if not div[i]:
            return INF

    ret = 0
    ret += eachtake(div[0], a)
    ret += eachtake(div[1], b)
    ret += eachtake(div[2], c)
    
    return ret


def solve():
    n, a, b, c = getList()
    li = []
    for i in range(n):
        li.append(getN())

    ans = INF
    for pat in range(4 ** n):
        tmp = eachpat(pat, a, b, c, li, n)
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
    # print(eachtake([333], 100))