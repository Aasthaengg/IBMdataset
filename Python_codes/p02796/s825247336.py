import sys
# from collections import defaultdict, deque
# import math
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
MOD = 10 ** 9 + 7
def solve():
    n = getN()
    arms = []
    for i in range(n):
        x, l = getList()
        arms.append((x-l, x+l))

    arms.sort()
    # print(arms)
    prev = -INF
    ans = n
    for arm in arms:
        if arm[0] < prev:
            ans -= 1
            if arm[1] <= prev:
                prev = arm[1]
        else:
            prev = arm[1]

    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
