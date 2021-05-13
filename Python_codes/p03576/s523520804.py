from itertools import accumulate
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}
n, k = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(n)]
X, Y = zip(*XY)
comp_X = compress(X)
comp_Y = compress(Y)
len_X = len(comp_X)
len_Y = len(comp_Y)
rev_X = {j:i for i, j in comp_X.items()}
rev_Y = {j:i for i, j in comp_Y.items()}
C = [[0]*(len_Y+1) for _ in range(len_X+1)]
for x, y in XY:
  C[comp_X[x]+1][comp_Y[y]+1] = 1
for i in range(1, len_X+1):
  C[i] = list(accumulate(C[i]))
C = list(zip(*C))
for j in range(1, len_Y+1):
  C[j] = list(accumulate(C[j]))
C = list(zip(*C))
def test(x1, x2, y1, y2):
  cnt = C[x2][y2] - C[x1][y2] - C[x2][y1] + C[x1][y1]
  if cnt >= k:
    temp = (rev_X[x2-1] - rev_X[x1]) * (rev_Y[y2-1] - rev_Y[y1])
    return temp
  return float("inf")
ans = float("inf")
for x1 in range(len_X):
  for x2 in range(x1+1, len_X+1):
    for y1 in range(len_Y):
      for y2 in range(y1+1, len_Y+1):
        ans = min(ans, test(x1, x2, y1, y2))
print(ans)