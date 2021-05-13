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
MOD = 1000000007

def solve():
    n = getN()
    anums = getList()
    bnums = getList()
    # if sum(anums) > sum(bnums):
    #     print("No")
    #     return

    pair = []
    for i, j in zip(anums, bnums):
        pair.append((i, j))

    pair.sort(key=lambda x:- x[0] + x[1])
    # print(pair)
    kosi = 0
    for a,b in pair:
        # a += kosi
        if b >= a:
            kosi -= (b-a) // 2 * 2
        else:
            kosi += (a - b) * 2
        # print(a, b, kosi)

    if kosi > 0:
        print("No")
        return
    else:
        print("Yes")
        return


def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
