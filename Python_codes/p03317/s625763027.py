import math

N, K = map(int, input().split(' '))

n = max(0, N - K)
print(1 + math.ceil(n / (K - 1)))
