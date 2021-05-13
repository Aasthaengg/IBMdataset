# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

X = ir()
answer = 1
for y in range(2, X):
    temp = y * y
    if temp > X:
        continue
    while temp * y <= X:
        temp *= y
    if temp > answer:
        answer = temp

print(answer)
