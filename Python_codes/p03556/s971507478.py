import math
N = int(input())
N_square_root = math.floor(math.sqrt(N))
result = 0
for i in range(N_square_root + 1):
    result = i * i
print(result)