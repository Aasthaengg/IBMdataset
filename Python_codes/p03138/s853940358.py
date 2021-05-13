import numpy as np
from functools import lru_cache

N,K = map(int,input().split())
A = np.array(input().split(),dtype=np.int64)

bit_cnt = [((A>>k)&1).sum() for k in range(50)]

@lru_cache(maxsize = None)
def F(K,k = 49):
  # K以下、k-bit目まで見た(inclusive)の和、最大値
  if k == -1:
    return 0
  bit = 1<<k
  # k-bitを使う
  x = 0
  if K >= bit:
    x = ((N-bit_cnt[k])<<k) + F(K-bit,k-1)
  # k-bitを使わない
  y = (bit_cnt[k]<<k) + F(min(K,bit-1),k-1)
  return max(x,y)

answer = F(K)
print(answer)
