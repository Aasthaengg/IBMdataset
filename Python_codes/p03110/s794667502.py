# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
answer = 0
for _ in range(N):
    x, u = sr().split()
    if u == 'JPY':
        answer += int(x)
    else:
        answer += float(x) * 380000
print(answer)
