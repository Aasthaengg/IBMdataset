from fractions import gcd
A, B = list(map(int,input().split()))
print(int((A * B)/gcd(A,B)))