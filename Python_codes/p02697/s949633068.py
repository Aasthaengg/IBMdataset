import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M = map(int, input().split())
res = []

def solve(l, r):
  global res
  if r <= l: return
  res.append((l, r))
  solve(l + 1, r - 1)


solve(1, M + 1)
solve(M + 2, M * 2 + 1)
for r in res: print(*r)