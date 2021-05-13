import sys

def q(i):
  print(i, flush=True)
  r = input()
  if r == 'Vacant':
    sys.exit()
  return r == 'Female'

n = int(input())

def go(a, b, ra):
  m = (a + b) // 2
  d = m - a + 1
  rm = q(m)
  if (ra == rm) == (d % 2 == 1):
    go(m, b, rm)
  else:
    go(a, m, ra)

ra = q(0)
rb = q(n - 1)
go(0, n - 1, ra)
