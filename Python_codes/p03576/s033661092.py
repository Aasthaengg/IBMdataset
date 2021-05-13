from itertools import groupby, accumulate, product, permutations, combinations
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i+1 for i, e in enumerate(XS)},{i+1: e for i, e in enumerate(XS)}

def solve():
  ans = float('inf')
  N, K = map(int, input().split())
  X,Y = [0]*N,[0]*N
  for i in range(N):
    X[i],Y[i] = map(int, input().split())
  x_c,x_r = compress(X)
  y_c,y_r = compress(Y)
  n_x = len(x_c)
  n_y = len(y_c)
  num = [[0]*(N+1) for _ in range(N+1)]
  for i in range(N):
    X[i] = x_c[X[i]]
    Y[i] = y_c[Y[i]]
    num[X[i]][Y[i]] += 1
  cum2 = [[0]*(N+1) for _ in range(N+1)]
  for i in range(1,N+1):
    for j in range(1,N+1):
      cum2[i][j] = cum2[i-1][j]+cum2[i][j-1]-cum2[i-1][j-1]+num[i][j]
  for x1,x2 in combinations(range(1,n_x+1),2):
    x_l = x_r[x2]-x_r[x1]
    for y1,y2 in combinations(range(1,n_y+1),2):
      k = cum2[x2][y2]+cum2[x1-1][y1-1]-cum2[x1-1][y2]-cum2[x2][y1-1]
      if k>=K:
        y_l = y_r[y2]-y_r[y1]
        ans = min(ans,x_l*y_l)
  return ans
print(solve())