import sys
readline = sys.stdin.readline

# ジャンプa : (i + 1, j + 2)
# ジャンプb : (i + 2, j + 1)

X,Y = map(int,readline().split())
DIV = 10 ** 9 + 7

from functools import reduce
def nCr(n,r,DIV):
  if r < n - r:
    r = n - r
  if r == 0:
    return 1
  f = lambda x,y:x*y%DIV
  X = reduce(f,range(n-r+1, n+1))
  Y = reduce(f,range(1, r+1))
  return X * pow(Y, DIV - 2, DIV) % DIV

# ジャンプaの回数は0～X回。これを全探索する
for a in range(X + 1):
  b = Y - a * 2
  if b < 0:
    continue
  if a + b * 2 == X and a * 2 + b == Y:
    print(nCr(a + b, a, DIV))
    break
else:
  print(0)
