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
    g = [[] for i in range(n)]
    ans = [-1 for i in range(n)]
    ji = [0 for i in range(n)]

    for i in range(n-1):
        a, b = getZList()
        g[a].append(b)
        g[b].append(a)
        ji[a] += 1
        ji[b] += 1

    cn = getList()
    cn.sort()
    h = []
    for i, j in enumerate(ji):
        heappush(h, (j, i))

    anss = 0

    for cnn in cn:
        while True:
            cj, ci = heappop(h)
            if ans[ci] == -1:
                ans[ci] = cnn
                anss += cnn * cj
                for gg in g[ci]:
                    ji[gg] -= 1
                    heappush(h, (ji[gg], gg))
                break

    print(anss)
    print(*ans)
def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()