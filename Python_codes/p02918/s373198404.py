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

def getmoji(k):
    return chr(ord("a") + k)

def main():
    n, k = getList()
    s = getS()

    ko, fuko = 0, 0
    for i, j in zip(s, s[1:]):
        if i == j:
            ko += 1
        else:
            fuko += 1
    print(ko + min(k*2, fuko))


if __name__ == "__main__":
    main()
   