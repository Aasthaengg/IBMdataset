n, a, b = map( int, input().split() )
if a > b:
  exit( print( 0 ) )
if n == 1:
  exit( print( 1 if a == b else 0 ) )
else:
  x = ( n - 1 ) * a + b
  y = ( n - 1 ) * b + a
  print( y - x + 1 )
