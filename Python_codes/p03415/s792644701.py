# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

C = [sr() for _ in range(3)]
answer = ''
for i in range(3):
    answer += C[i][i]

print(answer)
