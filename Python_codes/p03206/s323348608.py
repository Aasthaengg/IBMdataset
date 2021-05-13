# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

D = ir()
answer = 'Christmas'
time = 25 - D
for _ in range(time):
    answer += ' Eve'

print(answer)
