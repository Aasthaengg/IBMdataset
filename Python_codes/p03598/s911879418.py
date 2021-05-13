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
    n = getN()
    k = getN()
    nums = getList()

    ans = 0
    for i, num in enumerate(nums):
        ans += 2 * (min(abs(k - num), num))


    print(ans)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()