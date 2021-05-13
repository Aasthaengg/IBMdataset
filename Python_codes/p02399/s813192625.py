( a, b) = [ int(i) for i in input().split()] 

while True:
  d = a // b
  r = a % b
  f = a / b

  print( '{0:d} {1:d} {2:.5f}'.format( d, r, f))
  break