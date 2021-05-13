###template###
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
import heapq
INF = float("inf")
sys.setrecursionlimit(10**7)
# 4近傍（右, 下, 左, 上）
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W
def mi(): return map(int, input().split())
def ii(): return int(input())
###template###

S = input()

prevg = 0
prevp = 0

ans = 0
for enec in S:
  if prevg > prevp:
    #どちらでも出せるので勝つ方を出す
    if enec=='p':
      prevp += 1
    else:
      prevp += 1
      ans += 1
  else:
    #gを出すしかない
    prevg += 1
    if enec=='p':
      ans -= 1

print(ans)




