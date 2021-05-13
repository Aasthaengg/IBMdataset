import sys
import math

A,B = map(int,input().split())
if not ( 2 <= A <= 20 and 1 <= B <= 20 ): sys.exit()

if B == 1: print(0);sys.exit()
for I in range(math.ceil(B/A),21):
    if I*A-(I-1) >= B:
        print(I)
        sys.exit()