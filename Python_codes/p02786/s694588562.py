import sys
import math
ri = lambda: int(sys.stdin.readline())

h = ri()
a = int(math.log2(h)) + 1
print(2**a - 1)