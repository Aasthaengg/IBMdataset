import sys
from collections import defaultdict, deque

n, m = tuple(map(int, sys.stdin.buffer.readline().split()))
L = tuple(tuple(map(int, sys.stdin.buffer.readline().split())) for _ in range(m))

# print(n, m)
# print(L)

X = [n + 1] * (n + 1)
Y = [0] * (n + 1)
d = defaultdict(set)
for a, b in L:
    d[a].add(b)
    d[b].add(a)
# print(d)

X0 = X[0]
X[1] = 0
qu = deque([1])
while qu:
  i = qu.popleft()
  cost = X[i]
  for b in d[i]:
    if X[b] == X0:
      X[b] = cost + 1
      qu.append(b)

# print(X)
s = X[0]
try:
    X.index(X[0], 1)
except ValueError:
    print('Yes')
    # for v in X[2:]:
    #     print(v)
    for i in range(2, n + 1):
      c = X[i]
      for v in d[i]:
        # print(i, c, v, X[v], c - 1== X[v])
        if c - 1 == X[v]:
          Y[i] = v
          break
    for v in Y[2:]:
        print(v)
else:
    print('No')
