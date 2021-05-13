import math
N, R = map(int, input().split())
S = 0
if N>9:
     S = R
else:

    S = R + 100*(10-N)

print(S)