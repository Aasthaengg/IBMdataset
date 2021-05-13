## C - Modulo Summation
import fractions
N = int(input())
A = list(map(int, input().split()))

gcd = 0
for i in range(1, N):
    gcd = gcd * A[i] // fractions.gcd(gcd, A[i])
print( sum( [ (gcd - 1) % a for a in A] ) )