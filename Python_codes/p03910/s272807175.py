import sys
from collections import defaultdict, deque
import math

# import copy
from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def solve():
    n = getN()
    for i in range(1, 10000):
        if i * (i + 1) / 2 >= n:
            mx = i
            break
    # print(mx)
    ans = []
    for i in ([i for i in range(1, mx+1)[::-1]]):
        if n >= i:
            ans.append(i)
            n -= i


    if n != 0:
        sys.exit(1)

    for an in ans:
        print(an)


def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()