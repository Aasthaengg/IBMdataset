import sys
from collections import defaultdict as dd
from bisect import bisect_left as bl
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
res = 0
cs = [0] * (N + 1)
d = dd(list)
d[0].append(0)
for i in range(N):
  cs[i + 1] = cs[i] + A[i] - 1
  cs[i + 1] %= K
  d[cs[i + 1]].append(i + 1)
for i in range(N):
  x = bl(d[cs[i]], i) + 1
  y = bl(d[cs[i]], i + K)
  res += y - x
  #print(x, y, i)
  #print(res)
print(res)