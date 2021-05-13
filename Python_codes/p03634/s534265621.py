import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N = int(input())
e = dd(list)
for _ in range(N - 1):
  u, v, c = map(int, input().split())
  e[u].append((v, c))
  e[v].append((u, c))
Q, K = map(int, input().split())

dp = [10 ** 15] * (N + 1)
dp[K] = 0
s = [K]
while len(s):
  x = s.pop()
  for y, d in e[x]:
    if dp[y] > dp[x] + d:
      s.append(y)
      dp[y] = dp[x] + d

for _ in range(Q):
  u, v = map(int, input().split())
  print(dp[u] + dp[v])