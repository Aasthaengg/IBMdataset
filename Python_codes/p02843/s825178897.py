import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import decimal



if __name__ == "__main__":
    x = int(input())
    dp = [0]*101010
    dp[0] = 1
    for i in range(100,101010):
        for j in range(100,106):
            if dp[i-j]:
                dp[i] = 1
    print(dp[x])