import math
N = int(input())
while N>=1:
    max = math.ceil((-1+(1+8*N)**0.5)/2)
    print(max)
    N -= max