import sys
from collections import defaultdict as dd
from collections import deque as dq
input = sys.stdin.readline
N = int(input())
e = dd(list)
if N == 1:
  print(0)
  print(1)
  exit(0)
for _ in range(N - 1):
  u, v = map(int, input().split())
  e[u].append(v)
  e[v].append(u)
res = [0] * (N + 1)
x = list(map(int, input().split()))
x.sort()
print(sum(x[: -1]))
p = 0
dimp = 0
for i in range(N + 1):
  if len(e[i]) > dimp:
    p = i
    dimp = len(e[i])
Q = dq([])
Q.append(p)
vis = set()
while len(Q):
  q = Q.popleft()
  y = x.pop()
  vis.add(q)
  res[q] = y
  for n in e[q]:
    if n in vis: continue
    Q.append(n)

print(" ".join(list(map(str, res[1: ]))))