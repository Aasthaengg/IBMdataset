# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

def F(x):
    if x == 0:
        return ''
    if x % 2 == 0:
        return F(x//-2) + '0'
    else:
        return F((x-1)//-2) + '1'

N = ir()
answer = F(N)
if N == 0:
    answer = 0
print(answer)
