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
    nums = getList()
    
    b1, b2 = sorted(nums)[n//2 - 1], sorted(nums)[n//2]
    for i, num in enumerate(nums):
        if num <= b1:
            print(b2)
        else:
            print(b1)
def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
