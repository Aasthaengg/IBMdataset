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
    m, k = getList()
    if k == 0:
        ans = []
        for i in range(2**m):
           
            ans.append(i)
        
        for i in range(2**m-1, -1, -1):
            
            ans.append(i)

   
        print(*ans)
        return 
    if m <= 1 and k != 0:
        print(-1)
        return 
    if 2 ** m <= k:
        print(-1)
        return 
    ans = []
    for i in range(2**m):
        if i != k:
            ans.append(i)
    ans.append(k)
    for i in range(2**m-1, -1, -1):
        if i != k:
            ans.append(i)

    ans.append(k)
    print(*ans)

if __name__ == "__main__":
    main()
   