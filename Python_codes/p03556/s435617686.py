from math import sqrt
N=int(input())
x=int(sqrt(N))
if (x+1)**2<=N:
    print((x+1)**2)
else:
    print(x**2)