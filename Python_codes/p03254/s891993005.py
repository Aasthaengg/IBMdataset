import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np


def main(n, x, a):
  cnt = 0
  for j, i in enumerate(a):
    x -= i
    if x < 0:
      break
    elif j == n-1 and x > 0:
      break
    cnt += 1
  return cnt

n, x = map(int, readline().split())
a = np.sort(np.array(readline().split(), np.int64))
print(main(n, x, a))
