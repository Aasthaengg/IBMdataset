import sys
def kouyakusuu(a,b):
  A = max(a,b)
  B = min(a,b)
  d = A % B
  if d == 0:
    return B
  else:
    return kouyakusuu(B,d)
for line in sys.stdin.readlines():
  a,b = map(int,line.split())
  m = kouyakusuu(a,b)
  n = a*b//m
  print(m,n)