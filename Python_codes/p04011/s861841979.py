N=int(input())
K=int(input())
X=int(input())
Y=int(input())

print( (K * X)  + ( ( N-(K) ) * Y ) if N>K else (N * X ) )
