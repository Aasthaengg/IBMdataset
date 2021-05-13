import math
N, K = list(map(lambda k: int(k), input().split(" ")))
A = list(map(lambda a: int(a), input().split(" ")))

print(math.ceil((N - K) / (K - 1)) + 1) 