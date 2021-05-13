N, K = map( int, input().split() )

a, b = 0, 0 
for i in range( 1, N + 1 ):
  if i % K == 0:
    a += 1
  elif 2 * i % K == 0:
    b += 1

cnt = a ** 3 + b ** 3
print( cnt )