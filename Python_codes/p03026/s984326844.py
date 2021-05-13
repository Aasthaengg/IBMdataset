import sys
from collections import defaultdict as dd
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
e = dd(list)
inc = [0] * (N + 1)
for _ in range(N - 1):
  u, v = map(int, input().split())
  e[u].append(v)
  e[v].append(u)
  inc[u] += 1
  inc[v] += 1
x = 0
for i in range(1, N + 1):
  if inc[x] < inc[i]: x = i

c = list(map(int, input().split()))
c.sort()
ressum = sum(c[: -1])
vis = set()
res = [0] * (N + 1)
res[x] = c[-1]
def dfs(y):
  global vis
  global res
  global c
  res[y] = c.pop()
  for z in e[y]:
    if z in vis: continue
    vis.add(z)
    dfs(z)
vis.add(x)
dfs(x)
print(ressum)
print(*res[1: ])