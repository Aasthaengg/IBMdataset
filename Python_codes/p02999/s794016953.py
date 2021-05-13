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
S = input().rstrip()
N = int(input())
A = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.float64)
D = [int(input()) for _ in range(N)]
AB = [[int(x) for x in input().split()] for _ in range(N)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]
"""

X, A = map(int, input().split())
print(0 if X < A else 10)



# def main():

# if __name__ == '__main__':
#     main()
