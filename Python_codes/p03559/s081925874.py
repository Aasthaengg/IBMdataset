import sys
from bisect import bisect_right as br
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b.sort()
c.sort()
res = 0
bt = [0] * N
for j in range(N):
  y = b[j]
  k = br(c, y)
  bt[j] = N - k
csbt = [0] * (N + 1)
for i in range(N):
  csbt[i + 1] = csbt[i] + bt[i]
for i in range(N):
  x = a[i]
  j = br(b, x)
  if j < N:
    res += csbt[-1] - csbt[j]
print(res)