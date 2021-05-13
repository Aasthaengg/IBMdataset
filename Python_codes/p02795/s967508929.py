import math
H = int(input())
W = int(input())
l = max([H, W])
N = int(input())
print(math.ceil(N/l))
