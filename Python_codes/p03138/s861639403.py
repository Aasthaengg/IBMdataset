# coding: utf-8
import sys
from functools import lru_cache
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
A = np.array(lr(), np.int64)
limit = int(max(A.max(), K)).bit_length()
bit_cnt = [((A>>k)&1).sum() for k in range(limit)]

@lru_cache(None)
def solve(K, index):
    if index < 0:
        return 0
    bit = 1 << index
    # bitを使わない（整数Xのこの桁のbitは0）
    ret = (bit_cnt[index]<<index) + solve(min(K, bit-1), index-1)
    if bit <= K:
        ret = max(ret, ((N-bit_cnt[index])<<index) +  solve(K-bit, index-1))
    return ret

answer = solve(K, limit-1)
print(answer)

