N, K = map( int, input().split() )
MOD = 10 ** 9 + 7
 
def Combi( n, r ):
  n1 = 1
  n2 = 1
  for i in range( 1, r + 1 ):
    n1 = n1 * i % MOD
    n2 = n2 * ( n - i + 1 ) % MOD
  return ( n2 * pow( n1, MOD - 2, MOD ) ) % MOD
 
for i in range( 1, K + 1 ):
  if N - K + 1 >= i:
    print( ( Combi( N - K + 1, i ) * Combi( K - 1, i - 1 ) ) % MOD )
  else:
    print( 0 )