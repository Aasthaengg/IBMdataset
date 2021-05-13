import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1

N, D = map(int, input().split())
cover_region = 2 * D + 1
ans = N // cover_region
if N % cover_region > 0:
    ans += 1
print(ans)





# def main():

# if __name__ == '__main__':
#     main()
