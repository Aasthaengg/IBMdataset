# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
B = sr()
answer = dic[B]
print(answer)
# 04