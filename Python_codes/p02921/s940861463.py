import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1

def YesNo(flag): print('Yes' if flag else 'No')
def yesno(flag): print('yes' if flag else 'no')

""" Input
N = int(input())
N, A, B = map(int, input().split())
A = list(map(int, input().split()))
D = [int(input()) for _ in range(N)]
"""

S = input().rstrip()
T = input().rstrip()

counter = 0
for i in range(3):
    if S[i] == T[i]:
        counter += 1

print(counter)

# def main():


# if __name__ == '__main__':
#     main()
