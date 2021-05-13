import math
A,B,N = map(int,input().split())
if B>N:
    x = N
else:
    x = B-1

val = math.floor(A*x/B)
print(val)
