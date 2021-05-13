N, M = map(lambda x: int(x), input().split(' '))

import math
p = 100 * (N - M) + 1900 * M
p *= math.pow(2, M)

print(int(p))