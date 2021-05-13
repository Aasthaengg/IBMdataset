K,A,B = map(int,input().split())

if A + 2 < B:
    K2 = K - A + 1
    print( K2 // 2 * ( B - A ) + K2 % 2 + A)
else:
    print( 1 + K )
