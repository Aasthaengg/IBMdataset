# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 重なるところに注意
A, B, K = lr()
answer = [x for x in range(A, min(A+K, B+1))] + [x for x in range(max(B-K+1, A), B+1)]
answer = sorted(set(answer))
print('\n'.join(map(str, answer)))