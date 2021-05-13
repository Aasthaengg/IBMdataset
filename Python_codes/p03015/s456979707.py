import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    L = S()
    dp = [[0 for _ in range(2)] for ___ in range(len(L) + 1)]
    dp[0][0] = 1

    for i in range(len(L)):
        # place 0
        dp[i+1][1] += dp[i][1] * 2
        if int(L[i]) == 1:
            dp[i+1][0] += 2 * dp[i][0]
            dp[i+1][1] += dp[i][0]

        dp[i+1][0] %= mod
        dp[i+1][1] %= mod

        # place 1
        dp[i+1][1] += dp[i][1]
        if int(L[i]) == 0:
            dp[i+1][0] += dp[i][0]

        dp[i+1][0] %= mod
        dp[i+1][1] %= mod

    ans = dp[len(L)][0] + dp[len(L)][1]
    ans %= mod
    print(ans)
main()
