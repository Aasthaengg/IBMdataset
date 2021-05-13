import sys
import math
N = int(input())
if not (1 <= N <= 1000):
    sys.exit()

print(math.floor(N/3))