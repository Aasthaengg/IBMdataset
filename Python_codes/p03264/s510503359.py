# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

K = ir()
even = K // 2
odd = (K+1) // 2
answer = even * odd
print(answer)
