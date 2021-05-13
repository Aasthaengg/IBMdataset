N, K = map( int, input().split() )
V = list( map( int, input().split() ) )
 
max_number = 0
for A in range( K + 1 ):
  for B in range( K + 1 ):
    J = K - A - B
    if J < 0:
      continue
    if A + B >= N:
      hand = V
    else:
      hand = V[ : A ] + V[ N - B : ]
    hand = sorted( hand )
      
    hand_num = 0
    for i, j in enumerate(hand):
      if ( j > 0 ) or ( i == J ):
        hand = hand[ i: ]
        break
    max_number = max( max_number, sum( hand ))
print( max_number )