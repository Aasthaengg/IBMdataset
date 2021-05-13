import math
N, D = [int(s) for s in input().split(' ')]
print(math.ceil(N / (D * 2 + 1)))
