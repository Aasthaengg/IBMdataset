import fractions
A,B=map(int,input().split())
C=fractions.gcd(A,B)
print(int(A*B/C))