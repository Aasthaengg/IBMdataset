N,M = map(int,input().split())
import math
if N>M/2:
    print(int(M/2))
else:
    print(N+math.floor((M-2*N)/4))