from sys import stdin, setrecursionlimit
input = stdin.buffer.readline
setrecursionlimit(10 ** 7)

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, combinations_with_replacement
from itertools import accumulate
from math import ceil, sqrt, pi, radians, sin, cos

MOD = 10 ** 9 + 7
INF = 10 ** 18

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

X = int(input())
#S = input()
#N, M = map(int, input().split())
#A = list(map(int, input().split()))
#A = [int(input()) for _ in range(N)]
#ABC = [list(map(int, input().split())) for _ in range(N)]

print(lcm(X, 360) // X)
