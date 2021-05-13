import sys , math

N = int( input() )
A = list( map( int, input().split() ))

X = A[0]
for i in range(1,N):
    X = X ^ A[i]

ans = [ X ^ A[i] for i in range(N) ]
print( *ans )