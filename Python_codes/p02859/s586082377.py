import sys
from collections import defaultdict, deque
import bisect
from heapq import *
import math
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N, = map(int, input().split())
# N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# L = [list(input().strip())  for _ in range(N)]
# S = input().strip()

print(N ** 2)