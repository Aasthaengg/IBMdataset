import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np
mod = 998244353

n,s = map(int,readline().split())
a = list(map(int,readline().split()))
d = np.zeros(3001, np.int64)
d[0] = 1
for i in a:
  dd = [0]*i + list(d)
  d = d*2
  d += dd[:3001]
  d %= mod
print(d[s])