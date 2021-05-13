import math
N=int(input())
if math.sqrt(N)%1==0:
    print(N)
else:
    x=int(math.sqrt(N))
    print(x**2)