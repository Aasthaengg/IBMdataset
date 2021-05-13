import math
N,A,*T=map(int,open(0))
for t in T:
    A*=t//math.gcd(A,t)
print(A)