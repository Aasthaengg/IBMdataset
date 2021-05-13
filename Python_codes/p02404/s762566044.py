import sys
for l in sys.stdin:
  H, W = map(int,l.split())
  if H == 0 and W == 0:
    break
  for i,h in enumerate(range(H)):
      if i != 0 and i!=H-1:
          print ('#' + ('.' * (W -2)) +'#')
      else:
          print ('#' * W)
  print ('')