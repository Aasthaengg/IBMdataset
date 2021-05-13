import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1

""" Input
N, A, B = map(int, input().split())
A = list(map(int, input().split()))
D = [int(input()) for _ in range(N)]
"""

a = int(input())
s = input().rstrip()

if a >= 3200:
    print(s)
else:
    print('red')




# def main():


# if __name__ == '__main__':
#     main()
