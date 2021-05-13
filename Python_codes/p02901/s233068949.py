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
 

def makebin(arr):
    ret = 0
    for num in arr:
        ret += 2 ** (num - 1)

    return ret

def main():
    n, m = getList()
    dp = [INF] * (2 ** n)
    dp[0] = 0
    for i in range(m):
        a, b = getList()
        tgt = getList()
        kagi = makebin(tgt)
        for i, d in enumerate(dp):
            if d != -1:
                dp[i|kagi] = min(dp[i|kagi], d + a)
        # print(dp, kagi)

    if dp[-1] == INF:
        print(-1)
        return 
    print(dp[-1])
    # print(0&1)?






 
if __name__ == "__main__":
    main()
   