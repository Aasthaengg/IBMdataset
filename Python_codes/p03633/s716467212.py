
import sys
import numpy as np

n = int(sys.stdin.readline())
t = [int(sys.stdin.readline()) for _ in range(n)]

print(np.lcm.reduce(t))
