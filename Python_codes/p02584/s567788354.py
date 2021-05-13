x,k,d = [int(x) for x in input().split()]
if x < 0:
  x *= -1
def f():
  c = 0
  if x - (k * d) > 0:
    c = x - (k * d)
    return True
  return False

def check():
  l = 0
  r = k
  while l <= r:
    m = (r + l) // 2
    p = x - d * (2 * m - k)
    #print(l,m,r,p)
    if p > d:
      l = m + 1
    elif p < -1 * d:
      r = m - 1
    else:
      return m
  return m

if f():
  print(x - (k * d))
else:
  m1 = check()
  t = x - d * (2 * m1 - k)
  print(abs(t))
