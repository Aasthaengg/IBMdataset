import sys
from bisect import bisect_right as br
from bisect import bisect_left as bl
input = sys.stdin.readline
N = int(input())
mod = 10 ** 9 + 7
a = []
for _ in range(N): a.append(int(input()))
t = 0
table = [[] for _ in range(max(a) + 1)]
for i in range(N):
  if a[i] != t:
    t = a[i]
    table[a[i]].append(i)
dp = [0] * N
dp[0] = 1
#print(table)
#print(a)
for i in range(N):
  r = br(table[a[i]], i)
  l = bl(table[a[i]], i)
  if r < len(table[a[i]]) and (table[a[i]][l] == i):
    dp[table[a[i]][r]] += dp[i]
    dp[table[a[i]][r]] %= mod
    """
    for k in range(j, len(table[a[i]])):
      print(i, table[a[i]][k])
      dp[table[a[i]][k]] += dp[i]
      dp[table[a[i]][k]] %= mod
    """
  if i + 1 < N:
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
print(dp[-1])