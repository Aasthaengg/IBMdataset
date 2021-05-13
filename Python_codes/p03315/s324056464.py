# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = sr()
plus = S.count('+')
minus = 4 - plus
answer = plus - minus
print(answer)
