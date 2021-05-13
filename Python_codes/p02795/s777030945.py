import math
H = int(input())
W = int(input())
N = int(input())
large = max(H,W)
print(math.ceil(N/large))