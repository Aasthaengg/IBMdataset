# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
AB = [lr() for _ in range(M)]
AB.sort(key=lambda x: [x[0], x[1]])
cur = 0
answer = 0
for a, b in AB:
    if a >= cur:
        answer += 1
        cur = b
    if b < cur:
        cur = b

print(answer)
