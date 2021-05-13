# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
V = lr()
scores = set()
limit = min(N, K)
for i in range(limit+1): # iは左から取り出す個数
    for j in range(limit-i+1): # jは右から取り出す個数
        stone = V[:i] + V[N-j:]
        stone.sort()
        result = sum(stone)
        scores.add(result)
        for k in range(min(len(stone), K-(i+j))): # kは戻す個数
            if stone[k] >= 0:
                break
            result -= stone[k]
            scores.add(result)

answer = max(scores)
print(answer)
#