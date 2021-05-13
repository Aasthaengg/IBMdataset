import sys
from collections import defaultdict as dd
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
e = dd(list)
for _ in range(N - 1):
  u, v = map(int, input().split())
  e[u].append(v)
  e[v].append(u)
c = list(map(int, input().split()))
c.sort()
sm = sum(c) - c[-1]
res = [0] * (N + 1)
def dfs(x):
  global res
  res[x] = c.pop()
  for y in e[x]:
    if res[y]: continue
    dfs(y)
dfs(1)
print(sm)
print(*res[1: ])