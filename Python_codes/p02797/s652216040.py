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
    n, k, s = getList()
    if s > 10 ** 6:
        out = 1
    else:
        out = 10 ** 9
    ans = [out for i in range(n - k)] + [s for i in range(k)] #] + [0 for i in range(k-1)]

    print(*ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
