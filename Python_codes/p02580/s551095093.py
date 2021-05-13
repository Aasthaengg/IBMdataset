import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
@njit((i8[:],i8[:],i8[:],i8[:]), cache=True)
def main(lis_h,lis_w,bomb_h,bomb_w):
  bomb = {}
  for h,w in zip(bomb_h,bomb_w):
    bomb[(h,w)] = 1
  max_h = np.where(lis_h==lis_h.max())[0]
  max_w = np.where(lis_w==lis_w.max())[0]
  ans = lis_h.max()+lis_w.max()
  for h in max_h:
    for w in max_w:
      if (h,w) not in bomb:
        return ans
  return ans-1

H, W, M = map(int, input().split())
bombh = np.zeros(M, np.int64)
bombw = np.zeros(M, np.int64)
lis_h = np.zeros(H, np.int64)
lis_w = np.zeros(W, np.int64)
for i in range(M):
    h,w = map(int, input().split())
    h -= 1
    w -= 1
    bombh[i], bombw[i] = h,w
    lis_h[h] += 1
    lis_w[w] += 1
max_h = np.where(lis_h==lis_h.max())
max_w = np.where(lis_w==lis_w.max())
print(main(lis_h,lis_w,bombh,bombw))
