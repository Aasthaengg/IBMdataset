N, X, T = map(int,input().split())

A = N % X

if ( A ) == 0:
    print(( N // X ) * T )
elif ( N % X ) != 0:
    print(( N // X + 1 ) * T )