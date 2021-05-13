import sys
for l in sys.stdin:
  H, W = map(int,l.split())
  if H == 0 and W == 0:
    break
  for h in range(H):
    print (W * '#')
  print ('')