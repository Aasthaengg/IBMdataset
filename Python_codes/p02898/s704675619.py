import sys
from collections import defaultdict, deque, Counter
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
    n, k = getList()
    nums = getList()
    ans = 0
    for num in nums:
        if num >= k:
            ans += 1

    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()