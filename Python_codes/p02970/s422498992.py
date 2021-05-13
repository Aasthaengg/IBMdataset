import math
N, D = map(int, input().split())
l = 2 * D + 1
print(math.ceil(N / l))
