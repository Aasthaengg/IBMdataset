H = int(input())
W = int(input())
N = int(input())

import math

m = max(H,W)
print(math.ceil(N/m))