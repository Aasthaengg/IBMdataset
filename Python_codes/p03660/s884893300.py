import sys
from collections import defaultdict as dd
from collections import deque as dq
input = sys.stdin.readline
N = int(input())
e = dd(list)
for _ in range(N - 1):
  u, v = map(int, input().split())
  e[u].append(v)
  e[v].append(u)
d1 = [float("inf")] * (N + 1)
d1[1] = 0
Q = dq([])
Q.append(1)
while len(Q):
  p = Q.popleft()
  for q in e[p]:
    if d1[q] > d1[p] + 1:
      d1[q] = d1[p] + 1
      Q.append(q)
dn = [float("inf")] * (N + 1)
dn[N] = 0
Q.append(N)
while len(Q):
  p = Q.popleft()
  for q in e[p]:
    if dn[q] > dn[p] + 1:
      dn[q] = dn[p] + 1
      Q.append(q)
#print(d1, dn)
f = 0
for i in range(1, N + 1):
  if d1[i] <= dn[i]:
    f += 1
if f > N // 2: print("Fennec")
else: print("Snuke")