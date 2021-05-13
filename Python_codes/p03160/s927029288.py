N = int( input())
h = list( map( int, input().split()))

D = [ 0 ] + [ abs( h[1] - h[0] ) ]+[ 0 for i in range( N - 2 ) ]
for i in range( 1, N - 1):
  if i - 1 >= 0:
    D[ i + 1 ] = min( abs( h[ i + 1 ] - h[ i ] ) + D[ i ],
                      abs( h[ i + 1 ] - h [ i - 1 ] ) + D[i - 1 ])

print( D[ -1 ] )