import sys
import math
n, m = map(int, sys.stdin.buffer.readline().split())
a = tuple(map(int, sys.stdin.buffer.readline().split()))

lim = math.ceil(sum(a) / (4 * m))
c = sum(1 for aa in a if aa >= lim)
print('Yes' if c >= m else 'No')
