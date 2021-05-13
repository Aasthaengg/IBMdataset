import sys
from bisect import bisect_left as bl
from bisect import bisect_right as br
input = sys.stdin.readline
N = int(input())
table = [[] for _ in range(2 * pow(10, 5) + 1)]
a = []
t = 0
mod = 10 ** 9 + 7
for i in range(N):
  x = int(input())
  if t != x:
    table[x].append(i)
    t = x
  a.append(x)
#print(table[4], table[3])
dp = [0] * N
dp[0] = 1
for i in range(N):
  j = br(table[a[i]], i)
  k = bl(table[a[i]], i)
  if j < len(table[a[i]]) and (table[a[i]][k] == i):
    dp[table[a[i]][j]] += dp[i]
    dp[table[a[i]][j]] %= mod
  if i + 1 < N: 
    dp[i + 1] += dp[i]
    dp[i + 1] %= mod
  #print(dp)
print(dp[-1])