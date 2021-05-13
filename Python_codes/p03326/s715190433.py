import numpy as np
N, M, *L = map(int, open(0).read().split())
L = [np.array(m) for m in zip(*[iter(L)]*3)]
ans = 0
for i in range(8):
  X = []
  c = []
  for j in range(3):
    if i%2==1:
      c.append(-1)
    else:
      c.append(1)
    i >>= 1
  c = np.array(c)
  X = list(map(lambda x:sum(x*c), L))
  X.sort(reverse=True)
  ans = max(ans, sum(X[:M]))
print(ans)