# coding: utf-8
import sys
import numpy as np
from functools import lru_cache

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# bit毎で１と０の多い方の値、K以下でdfs
N, K = lr()
A = lr()
limit = max(max(A), K).bit_length()
X = [0] * (limit)
for a in A:
    for i in range(limit):
        if (a >> i) & 1:
            X[i] += 1

Y = [max(x, N-x) for x in X]

@lru_cache(None)
def cal(index, total):
    total += sum([y * 2 ** i for i, y in enumerate(Y[:index+1])])
    return total

@lru_cache(None)
def dfs(index, sum, y):
    if index == limit:
        return sum
    i = limit - 1 - index
    if y + 2 ** (i + 1) <= K:
        return cal(i, sum)
    ret = dfs(index+1, sum + X[i] * 2 ** i, y)
    if y + 2 ** i <= K:
        ret = max(ret, dfs(index+1, sum+(N-X[i])*2**i, y+2**i))
    return ret

answer = dfs(0, 0, 0)
print(answer)
