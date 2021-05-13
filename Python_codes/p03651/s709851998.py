INF = 10 ** 20
MOD = 10 ** 9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  heapq import heappop,heapify,heappush
from bisect import bisect_left
from functools import reduce
from fractions import gcd

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    if k > max(a):
        print('IMPOSSIBLE')
        return

    G = reduce(gcd,a)
    if k%G == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
if __name__ == '__main__':
    main()
