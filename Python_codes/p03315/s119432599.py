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
N = int(input())
N, A, B = map(int, input().split())
A = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.float64)
D = [int(input()) for _ in range(N)]
AB = [[int(x) for x in input().split()] for _ in range(N)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]
"""


S = input().rstrip()
ans = 0

for s in S:
    if s == '+':
        ans += 1
    else:
        ans -= 1

print(ans)

# def main():

# if __name__ == '__main__':
#     main()
