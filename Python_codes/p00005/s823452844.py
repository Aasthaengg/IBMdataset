import sys
for l in sys.stdin:
  a,b = map(int, l.split())
  x,y = (a,b) if a > b else (b,a)
  while x%y:
    m = x % y
    x,y = y,m
  print "%d %d" % (y, a*b/y)