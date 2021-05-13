A,P = map(int,input().split())

if ( A * 3 + P ) % 2 == 0:
  print(int( ( A * 3 + P ) / 2 ))
else:
  print( int(( A * 3 + P - 1) / 2 ))