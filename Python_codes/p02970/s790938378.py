import math
N, D = map(int, input().split(' '))
res = math.ceil(N / (D * 2 + 1))
print(res)