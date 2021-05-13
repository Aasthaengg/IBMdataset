import math

A, B, C = map(int,input().split())

if A // B == 0 & C != 0:
    print("NO")
if C % math.gcd(A,B) != 0:
    print("NO") 
else:
    print("YES")