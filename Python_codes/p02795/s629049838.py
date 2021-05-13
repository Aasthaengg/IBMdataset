import math
H = int(input())
W = int(input())
N = int(input())
if H < W:
    H = W
print(math.ceil(N/H))
