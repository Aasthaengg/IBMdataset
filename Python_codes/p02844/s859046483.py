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
 

def main():
    n = getN()
    S = getS()
    dp = [0] * (11*11*11)
    dp[0] = 1
    for c in S:
        tmp = [0] * (11*11*11)
        for i, d in enumerate(dp):
            if d == 1:
                tmp[i] = 1
                tmp[(i%121) * 11 + int(c) + 1] = 1

        dp = tmp
        # print(dp[-999:])
        # print(sum(dp[-999:]))

    print(sum(dp[(11*11):]))


 
if __name__ == "__main__":
    main()
   