import sys
import math
N,D = map(int,input().split())

if not ( 1 <= N <= 20 and 1 <= D <= 20 ): sys.exit()

print( math.ceil((N / (D*2+1))))