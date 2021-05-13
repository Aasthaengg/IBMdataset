import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

H, W = rl()
S = []
for i in range(H):
  s = rs()
  S.append(s + '#')
S.append('#'*(W+1))

tab = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(H):
  k = 0
  prev = -1
  for j in range(W+1):
    if S[i][j] == '#':
      n = j-prev-1
      while k < j:
        tab[i][k] += n
        k += 1
      tab[i][k] = 0
      k += 1
      prev = j

for j in range(W):
  k = 0
  prev = -1
  for i in range(H+1):
    if S[i][j] == '#':
      n = i-prev-1
      while k < i:
        tab[k][j] += n - 1
        k += 1
      tab[k][j] = 0
      k += 1
      prev = i

ans = 0
for i in range(H):
  for j in range(W):
    ans = max(ans, tab[i][j])
print(ans)
