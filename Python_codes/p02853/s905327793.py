import sys
from collections import defaultdict, deque
import bisect
from heapq import *
from math import factorial, ceil
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# N, M, = map(int, input().split())
# N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# L = [list(input().strip())  for _ in range(N)]
# S = input().strip()

N, M, = map(int, input().split())

ans = 0
if N == 1 and M == 1:
    ans += 400000

if N <= 3:
    ans += (4 - N) * 100000

if M <= 3:
    ans += (4 - M) * 100000

print(ans)