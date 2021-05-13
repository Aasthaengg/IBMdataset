N, K = map(int, input().split())

import math

print(math.ceil(N / K) - (N // K))