# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
D, X = lr()
choco = 0
for _ in range(N):
    a = ir()
    choco += 1 + (D-1) // a

answer = X + choco
print(answer)
